import json

kr = ''''''
en = ''''''

kr = kr.split('\n')
en = en.split('\n')
dict = {}
for k, e in zip(kr,en):
    dict[k] = e

file_path = "./tag_dict.json"

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(dict, file)