class Solution:

    def permute(self, nums:list[int])->list[list[int]]:
        result = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])
            
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        
        dfs(nums)
        return result


if __name__ == '__main__':
    sol = Solution()
    res = sol.permute([1,2,3])

    print(res)