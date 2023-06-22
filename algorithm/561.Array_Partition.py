'''
n개의 페어를 이용한 min(a, b)의 합으로
만들 수 있는 가장 큰 수의 합을 구하시오
'''

def array_part(num_arr : list)->int:
    num_arr.sort() # 오름차순 정렬
    jjaksu = num_arr[::2] # 짝수 index만 고르기 0 2 4 6 8 ...
    max_vl = sum(jjaksu)
    
    return max_vl

if __name__ == '__main__':
    print(array_part([3,5,1,6,7,1,2,3,5,7,9,11,1000000,1]))
    print(array_part([1,4,3,2]))