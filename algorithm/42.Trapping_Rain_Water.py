'''
막대기의 높이를 입력받아 
얼마만큼의 물이 쌓일수 있는지 계산하시오
ex) [1, 3, 5, 3, 1, 3] -> 2

'''

'''self'''

# def drop_water(num_arr : list)-> int:
#     max_vl = max(num_arr)
#     max_idx = num_arr.index(max_vl)

#     left = num_arr[:max_idx]
#     right = num_arr[max_idx + 1:]

#     left_max = left[0]
#     right_max = right[-1]
    
#     water = 0

#     for num in left:
#         if num > left_max:
#             left_max = num
#         else:
#             water += left_max - num
    
#     for num in right[::-1]:
#         if num > right_max:
#             right_max = num
#         else:
#             water += right_max - num
    
#     return water


'''two pointer'''

def drop_water(num_arr : list)->int:
    left = 0
    right = len(num_arr) - 1
    water = 0
    left_max, right_max = num_arr[left], num_arr[right]

    while left < right:
        left_max, right_max = max(num_arr[left], left_max),max(num_arr[right], right_max)

        if left_max <= right_max:
            water += left_max - num_arr[left]
            left += 1
        else:
            water += right_max - num_arr[right]
            right -= 1
    
    return water

'''stack'''

# def drop_water(num_arr : list)->int:
#     water = 0
#     stack = []
#     num = num_arr[0]
#     for i in range(len(num_arr)):
#         if num_arr[i] > num and stack:
#             mx = max(stack)
#             for height in stack:
#                 water += mx - height
#             stack = [stack[-1]]
#             num = num_arr[i]
#         else:
#             stack.append(num_arr[i])
    
#     return water

if __name__ == '__main__':
    lst = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(drop_water(lst))