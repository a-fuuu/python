# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None  # Handle empty list

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow  # Return the middle node
    
'''
런너 기법을 활용한 풀이
런너 기법 : slow, fast 포인터를 만들어 한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나
중간 위치, 길이 등을 판별할 때 유용하게 사용할 수 있다.
fast runner와 slow runner 간의 step을 2배 차이를 두는 식으로 지정한 후 fast runner가 리스트의 끝지점에 도착하면
slow는 정확히 리스트의 중간 지점에 도착하게 된다.
'''