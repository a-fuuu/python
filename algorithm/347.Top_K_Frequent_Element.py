'''
상위 K번 이상 등장하는 요소를 출력하시오

nums = [1,1,1,2,2,3]
K = 2
=> [1,2]
'''

class Solution:
    def k_freq_element(self, K:int, nums:list)->list:
        element_dict = {}
        for element in nums:
            if element in element_dict.keys():
                element_dict[element] += 1
            else:
                element_dict[element] = 1
        
        filtered_dict = filter(lambda item: item[1] >= K, element_dict.items())
        filtered_dict = dict(filtered_dict)
        return list(filtered_dict.keys())

if __name__ == '__main__':
    sol = Solution()
    print(sol.k_freq_element(2,[1,1,1,2,2,3]))