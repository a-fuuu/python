'''
덧셈하여 타겟을 만들 수 있는 배열 내의 두 인덱스를 리턴하시오
'''

'''brute force'''
def two_sum(num_arr : list, target : int)->list:
    
    for i in range(len(num_arr)-1):
        for j in range(1, len(num_arr)):
            if num_arr[i] + num_arr[j] == target:
                return [i, j]
            
if __name__ == '__main__':
    print(two_sum([1,2,3,4,5], 9))