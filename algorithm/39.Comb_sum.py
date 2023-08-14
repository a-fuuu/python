'''
숫자 집합을 조합하여 합이 target이 되는 원소를 나열하라 원소는 중복으로 사용 가능하다.

cand = [2,3,7]
target = 7

=> [2,2,3] [7]
'''

class Solution:
    def comb_sum(self, cand:list[int], target:int):
        result = []
        def dfs(pick:list[int], candi:list[int])->list[int]:
            if sum(pick) == target:
                result.append(pick)
                pick = []
                return
            elif sum(pick) > target:
                pick = []
                return
            for num in candi:
                pick.append(num)
                dfs(pick, candi)
        dfs([], cand)

        return result
    
if __name__ == '__main__':
    sol = Solution()
    res = sol.comb_sum([2,3,7], 7)
    print(res)
