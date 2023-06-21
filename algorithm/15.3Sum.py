'''
입력된 배열에서 
세 수의 합을 구해 0을 만들 수 있을경우 
해당하는 세 수를 리스트형태로 출력하시오
ex) 
in [-1, 0 , 1 , 2 , 3 , -5]
out [-1, 0, 1], [2, 3, -5]

먼저 정렬한다음 두개씩 합치고 합친 값이 0보다 크면 끝 작으면 계속 ㄱㄱ
'''

'''self result에 중복값 발생 양끝에서 오는게 아니라 비효율적'''
# def three_sum(num_arr : list)->list:
#     num_arr.sort() # 오름차순 정렬

#     left = 0
#     right = 1
#     result = []

#     while left < right and left != len(num_arr) - 2:
#         if num_arr[left] + num_arr[right] > 0:
#             return result
#         elif -(num_arr[left] + num_arr[right]) in num_arr:
#             result.append([num_arr[left], num_arr[right], -(num_arr[left] + num_arr[right])])

#         if right == len(num_arr) - 1:
#             left += 1
#             right = left + 1
        
#         right += 1

'''좌우 투포인터에서 점점 좁혀오는 형태로'''
def three_sum(num_arr : list)->list:
    num_arr.sort() # 오름차순 정렬

    left, right = 0, len(num_arr) - 1
    result = []

    while True:
        if num_arr[left] == num_arr[left + 1]:
            left += 1
        if num_arr[right] == num_arr[right - 1]:
            right -= 1
        
        if left > right:
            return result
        
        left_right_sum = num_arr[left] + num_arr[right]

        for num in num_arr[left+1:right]:
            if num + left_right_sum == 0:
                result.append([num_arr[left], num, num_arr[right]])
        
        if left_right_sum > 0:
            right -= 1
        else:
            left += 1
        
        
if __name__ == '__main__':
    print(three_sum([-1, 0 , 1 , 2 , 3 , -5]))