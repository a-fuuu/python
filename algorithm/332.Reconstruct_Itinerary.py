'''
[from,to] 로 구성된 항공권 목록을 이용하여 JFK에서 출발하는 여행 일정을 구성하라.
여러 일정이 있는 경우 사전 어휘 순으로 방문한다.
[[JFK, AUS], [AUS, AES], [AES,ASD]]
=> [JFK,AUS,AES,ASD]
'''
import collections

class Solution:
    def dfsrecon(self, plan:list[list[str]])->list[str]:
        graph = collections.defaultdict(list)

        for a,b in sorted(plan):
            graph[a].append(b)
        route = []
        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop(0))
            route.append(start)
        dfs('JFK')
        return route[::-1]

    ####################################################################################
    def reconstruct(self, plan:list[list[str]])->list[str]:
        result = {}
        for fromto in sorted(plan):
            if fromto[0] not in result:
                result[fromto[0]] = [fromto[1]]
            else:
                result[fromto[0]].append(fromto[1])
        path = []
        stack = ['JFK']
        while stack:
            while result[stack[-1]]:
                stack.append(result[stack[-1]].pop(0))
            path.append(stack.pop())
        return path[::-1]
    
    def recon(self, plan:list[list[str]])->list[str]:
        graph = collections.defaultdict(list)

        for a,b in sorted(plan):
            graph[a].append(b)
        
        route, stack = [], ['JFK']

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
        return route[::-1]

if __name__ == '__main__':
    sol = Solution() 
    print(sol.recon([['JFK', 'AUS'], ['AUS', 'AES'], ['AES','ASD']]))
    print(sol.dfsrecon([['JFK', 'AUS'], ['AUS', 'AES'], ['AES','ASD']]))
    #print(sol.reconstruct([['JFK', 'AUS'], ['AUS', 'AES'], ['AES','ASD']]))
    '''
    reconstruct 에서는 error가 발생하는데 defaultdict를 사용하지 않고 그냥 dictionary에 값을 할당한다면
    dictionary에 key 값이 없는 것에 접근하려고 할 경우 일반 dictionary 자료구조를 사용한다면 keyerror가 발생하여
    코드 자체가 돌아가지 않는 문제가 있었다. defaultdict의 경우에는 key가 없는 것에 접근할 경우 해당 key에 value가
    할당되어 있지 않더라도 keyerror를 발생시키지 않고 빈값을 return하여 keyerror를 발생시키지 않는다
    문제를 해결하려고 할때 적절한 자료구조를 사용해야 함을 상기시켜주는 문제였다. 또한 defaultdict에 대한 탐구도 해볼 필요성을 느꼈다.
    '''