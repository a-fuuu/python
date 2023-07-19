'''
인덱스 m에서 n까지를 역순으로 만들어라 인덱스는 1부터 시작한다
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse_linked_list2(self, m, n, head:ListNode)->ListNode:
        root = start = ListNode(None)
        root.next = head

        for i in range(m - 1):
            start = start.next
        end = start.next

        for i in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next
    

solution = Solution()
lst1 = ListNode(1)
lst1.next = ListNode(1)
lst1.next.next = ListNode(1)
lst1.next.next.next = ListNode(2)
lst1.next.next.next.next = ListNode(3)
lst1.next.next.next.next.next = ListNode(1500)

result = solution.reverse_linked_list2(3, 5, lst1)

current_node = result

while current_node:
    print(current_node.val)
    current_node = current_node.next