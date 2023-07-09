'''
역순으로 저장된 연결리스트의 숫자를 더하라
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def add_two_numbers(self, head1: ListNode, head2: ListNode):
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        num1 = ''
        num2 = ''
        lst1 = reverse(head1)
        lst2 = reverse(head2)

        current_node = lst1
        while current_node:
            num1 += current_node.val
            current_node = current_node.next
        current_node = lst2
        while current_node:
            num2 += current_node.val
            current_node = current_node.next
        
        
        return int(num1) + int(num2)
