

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def invert_bt(self, root: TreeNode)->int:
        if root:
            root.left, root.right = self.invert_bt(root.right), self.invert_bt(root.left)
            return root
        return None

def print_tree(root: TreeNode):
    if root is None:
        return
    print(root.data, end=" ")
    print_tree(root.left)
    print_tree(root.right)

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(None)
    root.left.right = TreeNode(None)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print_tree(root)
    res = sol.invert_bt(root)
    print_tree(root)