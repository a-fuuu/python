import re
import collections
'''
가장 흔한 단어 찾기
요구사항
1. 주어진 문자열에서 가장 흔한 단어를 찾는다
2. 구두점은 제외한다. ( 마침표, 쉼표 등  )
2. banned 된 문자열은 제외한다.
3. 결과값은 소문자로 제공한다. 
'''

def find_most_common_word(word : str, banned_word : list) -> str:
    banned_list = banned_word
    # list comprehension으로 한줄로 처리하기.
    words = [word for word in re.sub('[^\w]', ' ', word.lower()).split() if word not in banned_list]
    
    # # collections defaultdict 자료구조 사용하여 count 해결하기
    # counter = collections.defaultdict(int)
    # for word in words:
    #     counter[word] += 1
    
    # # max 함수 사용 key 설정 필요
    # return max(counter, key=counter.get)
    
    counter = collections.Counter(words)
    return counter.most_common(1)[0][0]
    

if __name__ == '__main__':
    ipt = 'Hello, bitches hello'
    banned_list = []
    print(find_most_common_word(ipt, banned_list))