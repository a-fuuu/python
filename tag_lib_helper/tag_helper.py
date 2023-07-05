import json
import requests

''' 함수 선언부 '''
def get_translate(text):
    '''
    네이버 파파고 API를 활용한
    한-영 번역을 수행하는 함수입니다.
    '''
    client_id = "" # <-- client_id 기입
    client_secret = "" # <-- client_secret 기입

    data = {'text' : text,
            'source' : 'ko',
            'target': 'en'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id":client_id,
            "X-Naver-Client-Secret":client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode==200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data.lower()
    else:
        print("Error Code:" , rescode)

def dictionary_mker(inp):
    a = inp.split(' ')
    result = []
    for item in a:
        try:
            result.append(dict[item].lower())
        except KeyError:
            print(f'{item} 이 단어 사전에 없습니다.')
    
    id = '_'.join(result).replace(' ','_')
    kr = inp.replace(' ', '')
    en = get_translate(kr)

    return f'{{ "id" : "{id}", "en" : "{en}", "kr" : "{kr}" }},'


# json file을 읽어 dictionary 형태로 변환
file_path = './tag_dict.json'
with open(file_path, 'r') as file:
    dict = json.load(file)


while True:
    print(dictionary_mker(input('추가될 TAG명을 단어를 공백으로 잘라서 작성해주세요 [ex) 평균 지연 일수] : ')))