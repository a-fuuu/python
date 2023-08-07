'''
중복 문자가 없는 가장 긴 부분 문자열의 길이를 구하라
abcabcbb
=> 3
bbbbbb
=> 1
'''

class Solution:
    def longest_substring(self, s:str)->int:
        sub = ''
        candidate = []
        for char in s:
            if char not in list(sub):
                sub += char
            elif sub not in candidate:
                candidate.append(sub)
                sub = char
            elif sub in candidate:
                sub = char
        return len(max(candidate, key=len))
    
    def longest_substring_sliding(self, s:str)->int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)
            used[char] = index

        return max_length


if __name__=='__main__':
    sol = Solution()
    print(sol.longest_substring('abcabcbb'))
    print(sol.longest_substring('bbbbbbb'))
    print(sol.longest_substring('pwwkew'))

    print(sol.longest_substring_sliding('abcabcbb'))
    print(sol.longest_substring_sliding('bbbbbbb'))
    print(sol.longest_substring_sliding('pwwkew'))