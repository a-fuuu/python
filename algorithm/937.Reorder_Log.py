"""
요구사항
1.로그의 가장 앞 부분은 식별자
2.문자로 구성된 로그가 숫자 로그보다 먼저온다.
3.식별자는 순서에 영향을 끼치지 않지만 문자가 동일할경우 식별자순으로 한다.
4.숫자로그는 입력 순서대로 처리한다.
"""

def is_digit(string : str) -> bool:
    '''
    입력받은 로그가 숫자로그인지 문자로그인지
    판별하여 TRUE, FALSE 값을 return 한다
    '''
    splitted_string = string.split(' ')
    if splitted_string[1].isalpha():
        result = False
    else:
        result = True
    
    return result

def reorder_log(log_list : list):
    '''
    로그 순서 정렬함수
    '''
    dig_log_list = []
    let_log_list = []
    
    for log in log_list:
        if is_digit(log):
            dig_log_list.append(log)
        else:
            let_log_list.append(log)
    
    sorted_let_log_list = sorted(let_log_list, key = lambda x : (x[4:], x[0]))
    
    sorted_log = sorted_let_log_list + dig_log_list
    
    print(sorted_log)
        

if __name__ == '__main__':
    log = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    log2 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    
    reorder_log(log)
    reorder_log(log2)