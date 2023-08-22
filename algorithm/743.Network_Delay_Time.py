'''
k부터 출발할 때 모든 노드가 신호를 받을 수 잇는 시간을 계산하라, 불가능할 경우 -1을 리턴한다
입력값 (u, v, w)는 각각 출발지, 도착지, 소요시간으로 구성되며 전체 노드의 개수는 N이다.
[[2,1,1], [2,3,1], [3,4,1]] N=4 k=2
=> 2
'''
import collections
import heapq

class Solution:
    def network_delay_time(self, node:list[list[int]], N:int, K:int):
        route = collections.defaultdict(list)
        for a, b, c in node:
            route[a].append((b, c))
        
        Q = [(0, K)]

        dist = collections.defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in route[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        if len(dist) == N:
            return max(dist.values())
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.network_delay_time([[2,1,1], [2,3,1], [3,4,1]], 4, 2))