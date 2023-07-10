'''
역순으로 저장된 연결리스트의 숫자를 더하라
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution():
#     def reverse(self, head: ListNode)->ListNode:
#         node, prev = head, None
#         while node:
#             next, node.next = node.next, prev
#             prev, node = node, next
#         return prev
        
#     def toList(self, node: ListNode)->list:
#         List = []
#         while node:
#             List.append(node.val)
#             node = node.next
#         return List
    
#     def toReversedLinkedList(self, result:str)->ListNode:
#         prev: ListNode = None
#         for r in result:
#             node = ListNode(r)
#             node.next = prev
#             prev = node
        
#         return node
    
#     def addTwoNumbers(self, l1 :ListNode, l2: ListNode) -> ListNode:
#         a = self.toList(self.reverse(l1))
#         b = self.toList(self.reverse(l2))
        
#         resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

#         return self.toReversedLinkedList(str(resultStr))

'''전가산기를 활용한 풀이'''
class Solution():
    def addTwoNumbers(self, l1:ListNode, l2:ListNode):
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next
            
            if l2:
                sum += l2.val
                l2 = l2.next
            
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        
        return root.next

solution = Solution()
lst1 = ListNode(1)
lst1.next = ListNode(1)
lst1.next.next = ListNode(1)
lst1.next.next.next = ListNode(2)

lst2 = ListNode(2)
lst2.next = ListNode(4)
lst2.next.next = ListNode(4)
lst2.next.next.next = ListNode(5)

result = solution.addTwoNumbers(lst1, lst2)

node = result

while node:
    print(node.val)
    node = node.next