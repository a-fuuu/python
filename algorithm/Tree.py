class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 이진 트리 생성 예제
root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.right.left = TreeNode("F")
root.right.right = TreeNode("G")

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        inorder_traversal(node.right)

# 중위 순회 실행
inorder_traversal(root)