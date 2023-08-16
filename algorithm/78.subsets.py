'''
모든 조합을 출력하시오
[1,2,3]
>> [[],[1], [1,2], [1,3], [2,3], [1,2,3]]
'''

class Solution():
    def subset(self, nums:list(int))->list[list[int]]:
        result = [[], nums]
        def dfs(path, index, candidates):
            if len(path) == len(nums):
                result.append(path)
                return
            elif len(path) == 0:
                result.append([])

            for element in candidates:
                path.append(element)
                
                