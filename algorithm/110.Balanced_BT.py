'''
이진트리 높이가 균형인지 판단하여라

*이진트리의 높이 균형 : 트리 노드들의 높이 차이가 1 이하인 이진트리
**BFS형태로 serialized 된 list를 받아서 결과를 출력해야 함
'''
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def check_balance(self, node:TreeNode)->bool:
        def recursive(node):
            if not node:
                return 0
            
            left = recursive(node.left)
            right = recursive(node.right)

            if left == -1 or \
                right == -1 or \
                abs(left - right) > 1:
                return -1
            return max(left, right) +1
        return recursive(node) != -1

if __name__ == '__main__':
    
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    sol = Solution()
    res = sol.check_balance(root)
    print(res)