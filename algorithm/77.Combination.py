'''
전체 수 n을 입력받아 k개의 조합을 return하라

n = 4 k = 2
=>
1,2
1,3
1,4
2,3
2,4
3,4
'''

class Solution:
    def combination(self, n:int, k:int):
        def dfs(picked:list[int], nums:list[int]):
            for num in nums:
                if len(picked) == k:
                    return picked
                else:
                    picked.append(num)
                    dfs(picked, nums.remove(num))

        candi = list(range(1, n+1))

        result = []

        result.append(dfs([candi.pop()], candi))

        return result
    

if __name__ == '__main__':
    sol = Solution()
    res = sol.combination(4, 2)
    print(res)