'''
괄호로 된 입력값이 올바른지 판별하시오
'''
from stack import Node, Stack

stack = []

table = {
    '}' : '{', 
    ']' : '[', 
    ')' : '(' }

class Solution:
    def valid_parentheses(self, s):
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.valid_parentheses('[]{}()'))
