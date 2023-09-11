class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    
    def merge_bt(self, root1: TreeNode, root2: TreeNode)->int:
        if root1 and root2:
            node = TreeNode(root1.data + root2.data)
            node.left = self.merge_bt(root1.left, root2.left)
            node.right = self.merge_bt(root1.right, root2.right)

            return node
        else:
            return root1 or root2
        
def print_tree(root: TreeNode):
    if root is None:
        return
    print(root.data, end=" ")
    print_tree(root.left)
    print_tree(root.right)

if __name__ == '__main__':
    sol = Solution()
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(0)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    root2 = TreeNode(5)
    root2.left = TreeNode(2)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(4)
    root2.right.left = TreeNode(5)
    root2.right.right = TreeNode(6)

    print_tree(root1)
    print()
    print_tree(root2)
    print()
    res = sol.merge_bt(root1, root2)
    print_tree(res)