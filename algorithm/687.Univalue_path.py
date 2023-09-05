'''
동일한 값을 가진 가장 긴 경로를 찾아라
Input: root = [5,4,5,1,1,null,5]
Output: 2
'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    result:int = 0
    def max_unipath(self, root: TreeNode)->int:
        

        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.data == node.data:
                left += 1
            else:
                left = 0
            
            if node.right and node.right.data == node.data:
                right += 1
            else:
                right = 0
            
            self.result = max(self.result, left + right)
            return max(left, right)
        
        dfs(root)
        return self.result
        

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(3)
    root.left.left = TreeNode(None)
    root.left.right = TreeNode(None)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(3)
    res = sol.max_unipath(root)
    print(res)