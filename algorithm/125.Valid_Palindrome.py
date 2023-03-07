'''
주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로한다.
'''

class Palindrome:
    def __init__(self, s: str) -> bool:
        self.s = s

    def isPalindrome(self):
        strs = []
        for s in self.s:
            if s.isalnum():
                strs.append(s)

        while strs:
            if strs.pop(0) != strs.pop():
                return False
            return True

ipt = input().lower()

Palindrome(ipt)