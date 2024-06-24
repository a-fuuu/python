import os
import shutil

def file_download():
    source_path = "/mnt/c/Users/전준표/OneDrive - 하이퍼라운지/Shared Documents/General/☀︎ 팀 회의 자료/DE_데이터팀/400. Tag Library/Tag_library_추가요청.xlsx"
    local_path = "/home/junpyo/airflow"
    local_filename = "Tag_library_추가요청.xlsx"

    # 기존 파일 삭제
    if os.path.exists(os.path.join(local_path, local_filename)):
        os.remove(os.path.join(local_path, local_filename))

    # 파일 복사
    shutil.copyfile(source_path, os.path.join(local_path, local_filename))