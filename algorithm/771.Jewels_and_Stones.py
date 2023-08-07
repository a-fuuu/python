'''
J는 보석이고 S는 돌이다 
S 중 보석에 해당하는 것이 몇개가 있는지 세어보시오

ex) J = 'aA'
    S = 'aAAbbb'
-> 3
'''
from collections import Counter

class Solution:
    # Counter를 사용한 풀이
    def count_jewels(self, J:str, S:str)->int:
        counter = Counter(S)
        count = 0
        for jewel in J:
            count += counter[jewel]
        
        return count
    
    # Hash Map을 사용한 풀이
    def hash_jewels(self, J:str, S:str)->int:
        freqs = {}
        count = 0

        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        for char in J:
            if char in freqs:
                count += freqs[char]
        
        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.count_jewels('aA', 'aAAbbb'))
    print(sol.hash_jewels('aA', 'aAAbbb'))