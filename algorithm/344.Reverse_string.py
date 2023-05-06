import time

def reverseString_by_twopointer(string : str)->str :
    '''
    투포인터를 활용한 문자열 뒤집기
    '''
    left_pointer = 0
    right_pointer = len(string) - 1
    
    string_lst = list(string)
    
    while left_pointer < right_pointer:
        '''좌우 포인터에 위치한 것 끼리 자리 바꾸기'''
        string_lst[left_pointer], string_lst[right_pointer] = string_lst[right_pointer], string_lst[left_pointer]
        left_pointer += 1
        right_pointer -= 1
    
    reversed_string = ''.join(string_lst)
    
    return reversed_string

def reverseString_by_slicing(string : str)->str:
    '''
    파이썬 슬라이싱을 활용한 문자열 뒤집기
    '''
    string_lst = list(string)
    reversed_string = ''.join(string_lst[::-1])

    return reversed_string

if __name__ == '__main__':
    s = input()
    
    start = time.time()
    print(reverseString_by_twopointer(s))
    end = time.time()
    
    print(f'투포인터를 활용한 문자열 뒤집기에 소요된 시간은 {end-start}초')
    
    start = time.time()
    print(reverseString_by_slicing(s))
    end = time.time()
    
    print(f'슬라이싱을 활용한 문자열 뒤집기에 소요된 시간은 {end-start}초')