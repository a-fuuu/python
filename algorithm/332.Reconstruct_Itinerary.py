'''
[from,to] 로 구성된 항공권 목록을 이용하여 JFK에서 출발하는 여행 일정을 구성하라.
여러 일정이 있는 경우 사전 어휘 순으로 방문한다.
[[JFK, AUS], [AUS, AES], [AES,ASD]]
=> [JFK,AUS,AES,ASD]
'''

class Solution:
    def reconstruct(self, plan:list[list[str]])->list[str]:
        