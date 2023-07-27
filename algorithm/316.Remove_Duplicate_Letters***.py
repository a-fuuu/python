import collections
'''
중복된 문자를 제거하고 사전식으로 나열하라
bcacb
=> acb

cbacdcbc
a + f(cdcbc)
    b c d
    b c
    b c d
a + c + f(db)
    b d
    b
    b d
a + c + d + f(b)
a + c + d + b
acdb
=>acdb
'''


class Solution:
    # recursive
    def duplicate_order(self, s):
        for char in sorted(set(s)): # a b c d
            suffix = s[s.index(char):] 
            if set(s) == set(suffix):
                return char + self.duplicate_order(suffix.replace(char,''))
        return ''
    
    # stack
    def duplicate_order_stack(self, s:str):
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)

if __name__ == '__main__':
    solution = Solution()
    print(solution.duplicate_order('cbacdcbc'))
    print(solution.duplicate_order_stack('cbacdcbc'))