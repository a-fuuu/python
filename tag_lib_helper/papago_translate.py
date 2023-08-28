import requests

class Translator:
    def translate(self, text):
        '''
        네이버 파파고 API를 활용한
        한-영 번역을 수행하는 함수입니다.
        '''

        with open('./key.txt', 'r') as key_file:
            contents = key_file.read()
            contents = contents.split('\n')
            client_id = contents[0]
            client_secret = contents[1]

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