import json
from papago_translate import Translator

translator = Translator()

def dictionary_maker(inp):
    words = inp.split(' ')
    result = []
    file_path = './tag_dict.json'
    with open(file_path, 'r+') as file:
        dict = json.load(file)
    for word in words:
        try:
            result.append(dict[word].lower())
        except KeyError:
            dict[word] = translator.translate(word)
            file.write(f'{word}:{translator.translate(word)}')
            print(f'{word} 단어를 사전에 추가했습니다.')
            result.append(dict[word].lower())
            
    
    id = '_'.join(result).replace(' ','_')
    kr = inp.replace(' ', '')
    en = translator.translate(kr)
    return f'{{ "id" : "{id}", "en" : "{en}", "kr" : "{kr}" }},'

# json file을 읽어 dictionary 형태로 변환


if __name__ == '__main__':
    inp = input('추가하고자 하는 Tag 명을 입력해주세요 : ')
    print(dictionary_maker(inp))