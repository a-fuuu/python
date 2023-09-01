import collections

class Solution:
    def max_dep(self, root: Treenode)->int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1

            for _ in range(len(queue)):
                cur_root = queue.popleft()

        
        return depth