import os
import shutil

def file_download():
    path = "/mnt/c/Users/전준표/OneDrive - 하이퍼라운지/Shared Documents/General/☀︎ 팀 회의 자료/DE_데이터팀/400. Tag Library/Tag_library_추가요청.xlsx"

    filename = os.path.basename(path)

    local_path = "./"

    # 최신 tag library 요청 리스트를 받기 위해 파일이 존재하는 경우 삭제
    if os.path.exists("./Tag_library_추가요청.xlsx"):
        os.remove("./Tag_library_추가요청.xlsx")
    
    # 파일을 local path에 복사합니다. Onedrive 경로의 파일은 접근 권한 이슈가 있음
    shutil.copyfile(path, os.path.join(local_path, filename))


if __name__ == '__main__':
    file_download()