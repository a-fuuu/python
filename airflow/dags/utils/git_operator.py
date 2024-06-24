import subprocess
import json
import os
def git_pull_push(**kwargs):
    ti = kwargs['ti']
    update_required = ti.xcom_pull(task_ids='etl', key='version')
    
    if True:
        version = update_required  # 문자열을 다시 JSON으로 변환
        print(f'업데이트 사항이 있습니다. version : {version}')

        change_directory = 'cd /home/junpyo/airflow/modelmapping/ && git pull'
        subprocess.call(change_directory, shell=True)

        # Define the working directory
        working_directory = "/home/junpyo/airflow/modelmapping/"
        
        add_command = "git add ."
        subprocess.run(add_command, shell=True, cwd=working_directory)

        commit_command = 'git commit -m "tag lib update"'
        subprocess.call(commit_command, shell=True, cwd=working_directory)

        push_command = 'git push'
        subprocess.call(push_command, shell=True, cwd=working_directory)
    
    local_path = "/home/junpyo/airflow"
    local_filename = "Tag_library_추가요청.xlsx"

    # 기존 파일 삭제
    if os.path.exists(os.path.join(local_path, local_filename)):
        os.remove(os.path.join(local_path, local_filename))