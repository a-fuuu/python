'''
주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로한다.
'''

import collections
import re
import time
# 
class Palindrome:
    def __init__(self, s: str) -> bool:
        self.s = s

    def isPalindrome_pop(self):
        strs = []
        for s in self.s:
            if s.isalnum():
                strs.append(s)

        while strs:
            if strs.pop(0) != strs.pop():
                return print(False)
            return print(True)

    def isPalindrome_deque(self):
        strs = collections.deque()
        for s in self.s:
            if s.isalnum():
                strs.append(s)
        
        while strs:
            if strs.popleft() != strs.pop():
                return print(False)
            return print(True)
    
    def isPalindrome_slicing(self):
        s = re.sub('[^a-z0-9]', '', self.s)
        return print(s == s[::-1])

ipt = input().lower()

start_time = time.time()
Palindrome(ipt).isPalindrome_pop()
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
Palindrome(ipt).isPalindrome_deque()
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
Palindrome(ipt).isPalindrome_slicing()
end_time = time.time()
print(end_time - start_time)