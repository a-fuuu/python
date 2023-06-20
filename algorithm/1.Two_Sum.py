'''
덧셈하여 타겟을 만들 수 있는 배열 내의 두 인덱스를 리턴하시오
'''

'''brute force'''
# def two_sum(num_arr : list, target : int)->list:
    
#     for i in range(len(num_arr)-1):
#         for j in range(1, len(num_arr)):
#             if num_arr[i] + num_arr[j] == target:
#                 return [i, j]

'''in을 활용한 탐색'''

# def two_sum(num_arr : list, target : int)->list:

#     for i, n in enumerate(num_arr):
#         target_diff = target - n
#         if target_diff in num_arr[i+1:]:
#             return [num_arr.index(n), num_arr[i+1:].index(target_diff) + (i+1)]

'''key 값을 통한 조회'''

# def two_sum(num_arr : list, target : int)->list:
#     dict = {}
#     for i, n in enumerate(num_arr):
#         dict[n] = i
    
#     for i, n in enumerate(num_arr):
#         if target - n in dict and i != dict[target - n]:
#             return [i, dict[target -n]]

'''key 값을 통한 조회 v2'''

def two_sum(num_arr : list, target : int)->list:
    dict = {}
    
    for i, n in enumerate(num_arr):
        if target - n in dict and i != dict[target - n]:
            return [i, dict[target -n]]
        dict[n] = i

if __name__ == '__main__':
    print(two_sum([1,2,3,4,5], 9))


