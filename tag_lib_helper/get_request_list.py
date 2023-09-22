import os
import shutil
import pandas as pd
import openpyxl

# 파일의 경로를 지정합니다
path = "/mnt/c/Users/전준표/OneDrive - 하이퍼라운지/Shared Documents/General/☀︎ 팀 회의 자료/DE_데이터팀/400. Tag Library/통합 문서.xlsx"

filename = os.path.basename(path)

local_path = "./"

# 최신 tag library 요청 리스트를 받기 위해 파일이 존재하는 경우 삭제
if os.path.exists("./통합 문서.xlsx"):
    os.remove("./통합 문서.xlsx")

# 파일을 local path에 복사합니다. Onedrive 경로의 파일은 접근 권한 이슈가 있음
shutil.copyfile(path, os.path.join(local_path, filename))




##################################여기서부터#################################

excel_file_path = "./통합 문서.xlsx"

# Excel 파일을 데이터프레임으로 읽어오기
df = pd.read_excel(excel_file_path, header=1)

# 처리상태가 비어있는 항목들 선택
todo = df[df['처리상태'].isna()]

todo = todo[['처리상태', '내용']]

# 데이터프레임 출력 (옵션)
# print(todo)
for row in todo['내용']:
    print(row)

# Load the Excel workbook
workbook = openpyxl.load_workbook("./통합 문서.xlsx")

# Select the worksheet you want to modify
worksheet = workbook['Sheet1']

cell = worksheet.cell(row=2, column=3)  # Row 2, Column C

# Change the value of the cell
cell.value = 'TEST'

# Save the modified workbook
workbook.save('통합 문서.xlsx')

path = "/mnt/c/Users/전준표/OneDrive - 하이퍼라운지/Shared Documents/General/☀︎ 팀 회의 자료/DE_데이터팀/400. Tag Library/"
filename = os.path.basename(excel_file_path)
if os.path.exists("/mnt/c/Users/전준표/OneDrive - 하이퍼라운지/Shared Documents/General/☀︎ 팀 회의 자료/DE_데이터팀/400. Tag Library/통합 문서.xlsx"):
    os.remove("/mnt/c/Users/전준표/OneDrive - 하이퍼라운지/Shared Documents/General/☀︎ 팀 회의 자료/DE_데이터팀/400. Tag Library/통합 문서.xlsx")

shutil.copyfile(excel_file_path, os.path.join(path, filename))
