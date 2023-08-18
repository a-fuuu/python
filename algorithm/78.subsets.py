'''
모든 조합을 출력하시오
[1,2,3]
>> [[],[1], [1,2], [1,3], [2,3], [1,2,3]]
'''

class Solution():
    def subset(self, nums:list[int])->list[list[int]]:
        result = []
        def dfs(path, index):
            result.append(path)

            for i in range(index, len(nums)):
                dfs(path + [nums[i]], i+1)
        
        dfs([], 0)
        return result

if __name__ == '__main__':
    sol = Solution()
    res = sol.subset([1,2,3,4,5,6,7])
    print(res)