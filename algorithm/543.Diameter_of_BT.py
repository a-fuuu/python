import collections

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    longest:int = 0

    def max_dia(self, root: TreeNode)->int:
        def dfs(node: TreeNode)->int:
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)
            
            return max(left, right) + 1
        dfs(root)
        return self.longest

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(None)
    root.left.right = TreeNode(None)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    res = sol.max_dia(root)
    print(res)