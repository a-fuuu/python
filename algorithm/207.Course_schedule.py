'''
0을 완료하기 위해서는 1을 끝내야한다는 것을 [0,1]과 같이 표현하는 코스가 있을 때
이 코스가 완료 가능한 것인지 판별하라.
2, [[1,0]] -> True
2, [[1,0], [0,1]] -> False 순환 발생
'''
import collections

class Solution():
    def course_schedule(self, numcourse:int ,course:list[list[str]]):
        graph = collections.defaultdict(list)
        traced = set()
        for a,b in course:
            graph[a].append(b)
        
        def dfs(i):
            if i in traced:
                return False
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)

            return True
        
        for c in list(graph):
            if not dfs(c):
                return False
        return True
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.course_schedule(2, [[1,0], [0,1]]))
    print(sol.course_schedule(2, [[1,0]]))
    print(sol.course_schedule(2, [[0,1], [0,2], [1,2]]))