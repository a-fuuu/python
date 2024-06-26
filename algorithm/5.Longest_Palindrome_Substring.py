"""
가장 긴 팰린드롬 문자열 부분을 출력하시오
babad => bab, aba
cbbd => bb
"""

def palindrome(s : str)->str:
    
    def expand(left : int, right : int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]


    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ''

    for i in range(len(s) -1):
        result = max(result,
                        expand(i, i+1),
                        expand(i, i+2),
                        key = len)
    return result


if __name__ == '__main__':
    print(palindrome('asdsaaaaaaaaaaa'))