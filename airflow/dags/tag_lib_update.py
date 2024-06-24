from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from utils.file_downloader import file_download
from utils.tag_processor import extract_translate_append
from utils.git_operator import git_pull_push

default_args = {
    'start_date': days_ago(0),
    'email_on_failure' : False,
    'retries' : 1,
    'timezone' : 'KST',
    'catchup' : False,
}

dag = DAG(
    dag_id='Tag_Library_update',
    default_args=default_args,
    schedule_interval="*/10 * * * *",
    catchup = False
)

excel_download = PythonOperator(
    task_id='file_download',
    python_callable= file_download,
    dag=dag
)

etl = PythonOperator(
    task_id='etl',
    python_callable=extract_translate_append,
    provide_context=True,
    dag=dag
)

git_sync = PythonOperator(
    task_id='git_sync',
    python_callable=git_pull_push,
    provide_context=True,
    dag=dag
    )

excel_download >> etl >> git_sync