'''
정렬된 두 리스트를 합치기
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

solution = Solution()
lst1 = ListNode(1)
lst1.next = ListNode(1)
lst1.next.next = ListNode(1)
lst1.next.next.next = ListNode(2)
lst1.next.next.next.next = ListNode(3)
lst1.next.next.next.next.next = ListNode(1500)

lst2 = ListNode(2)
lst2.next = ListNode(4)
lst2.next.next = ListNode(4)
lst2.next.next.next = ListNode(5)
lst2.next.next.next.next = ListNode(7)
lst2.next.next.next.next.next = ListNode(10)

result = solution.mergeTwoLists(lst1, lst2)

current_node = result

while current_node:
    print(current_node.val)
    current_node = current_node.next