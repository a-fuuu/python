'''
인덱스 m에서 n까지를 역순으로 만들어라 인덱스는 1부터 시작한다
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse_linked_list2(self, m, n, head:ListNode)->ListNode:
        node = head
        
        while 