from datetime import datetime, timedelta
import subprocess

# 시작 날짜와 종료 날짜 정의
start_date = datetime(2023, 10, 1)
end_date = datetime(2023, 10, 10)

# 날짜 간격을 설정
day_delta = timedelta(days=1)
tenant_code = 'c4f77e00'
source_name = 'rpa'
source_code = 'sf43cba7'


# 시작 날짜부터 종료 날짜까지 반복
current_date = start_date

f = open("untitled.txt", "w")
f.write("")

while current_date <= end_date:
    gen_date = current_date.strftime('%Y%m%d') + '110000'
    gsutil_command = f'gsutil cp untitled.txt gs://hyperlounge-{tenant_code}-foldersync/{source_name}/{source_code}/{gen_date}/'
    subprocess.call(gsutil_command, shell=True)
    current_date += day_delta