'''
1이 육지 0이 바다라고 할때 섬의 개수를 출력하시오

111
100
100
000
111

=> 2

111
110
010
010
111

=> 1
'''

class Solution:
    def num_of_island(self, map:list[list[str]]):
        def dfs(i, j):
            if i < 0 or i >= len(map) or j < 0 or j >= len(map[0]) or map[i][j] != '1':
                return

            map[i][j] = '0' # 이부분 덕분에 count가 조절됐음
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count, map
    

if __name__ == '__main__':
    sol = Solution()

    ans = sol.num_of_island([['1', '1', '0'],
                        ['0', '0', '1'],
                        ['0', '1', '0']])
    
    print(ans)