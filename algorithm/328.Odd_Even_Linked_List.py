'''
연결 리스트를 홀수 노드 다음에 짝수가 오도록 재구성하여라
'''

# 연결리스트 class
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def odd_next_even(self, head:ListNode):
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head
    
solution = Solution()
lst2 = ListNode(1)
lst2.next = ListNode(2)
lst2.next.next = ListNode(3)
lst2.next.next.next = ListNode(4)
lst2.next.next.next.next = ListNode(5)

result = solution.odd_next_even(lst2)

node = result

while node:
    print(node.val)
    node = node.next