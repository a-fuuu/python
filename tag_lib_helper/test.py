# from konlpy.tag import Okt
import json
# text = "계좌구분명"

# okt = Okt()
# t = ' '.join(okt.morphs(text))


# print(t)


file_path = '../../../professional/modelmapping/de_server/db_to_excel/hl_standards_new_tag.json'
    
with open(file_path, encoding='utf-8') as f:
    data = json.load(f)

subject_area = data["hl_standards_tag"][0]['subject_area']
sub = [x['id'] for x in subject_area]

result = []
for s in sub:
    element = data['hl_standards_tag'][0]['analysis_item'][0]['key_tag'][0][s]
    kr = [kr['kr'] for kr in element]
    result = result + kr

print(sub)

print(result)
