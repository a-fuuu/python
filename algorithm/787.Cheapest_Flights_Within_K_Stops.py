'''
시작점에서 도착점까지의 가장 저렴한 가격을 계산하되 K개의 경유지 이내에 도착하는 
가격을 리턴하여라 경로가 존재하지 않을 경우 -1을 리턴한다.

n = 3 edges = [[0,1,100],[1,2,100],[0,2,500]]
src(출발지)=0, dst(도착지)=2, K=0
=> 500
'''
import sys
import heapq
import collections

class Solution:
    def cheapeast_flight(self, n:int, edges:list[list[int]], src:int, dst:int, K:int):
        graph = collections.defaultdict(list)
        for src, dst, cst in edges:
            graph[src].append((dst, cst))
        
        Q = [(0, src, K)]
        while Q:
            cost, node, k = heapq.heappop(Q)
            if node == dst:
                return cost
            if k >= 0:
                for v,w in graph[node]:
                    alt = cost + w
                    heapq.heappush(Q, (alt, v, k - 1))
        return -1
    

if __name__ == '__main__':
    sol = Solution()
    result = sol.cheapeast_flight(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)
    print(result)
    result = sol.cheapeast_flight(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 2)
    print(result)