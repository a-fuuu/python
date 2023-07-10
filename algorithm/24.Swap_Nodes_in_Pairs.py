'''연결리스트를 입력받아 페어 단위로 스왑하라
ex)
1->4->5->7
4->1->7->5
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def pair_swap(self, head:ListNode)->ListNode:
        
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        
        return head
    

    def pair_swap_2(self, head:ListNode)->ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next
        
        return root.next



        

solution = Solution()

lst2 = ListNode(2)
lst2.next = ListNode(4)
lst2.next.next = ListNode(4)
lst2.next.next.next = ListNode(5)

result = solution.pair_swap_2(lst2)


while result:
    print(result.val)
    result = result.next