'''
중복된 문자를 제거하고 사전식으로 나열하라
bcacb
=> acb
'''

# recursive
class Solution:
    def duplicate_order(self, s):
        stack = []
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.duplicate_order(suffix.replace(char,''))
        return ''
