'''
이진트리를 직렬화, 역직렬화 하시오
'''

import collections


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root:TreeNode)->str:
        queue = collections.deque([root])
        result = ['#']
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.data))
            else:
                result.append('#')
        return ' '.join(result)

    def deserialize(self, data:str):
        if data == '# #':
            return None
        nodes = data.split()

        root = TreeNode(nodes[1]) # 직관성을 위해 data 맨 앞에 #을 넣어두었기 때문에 index가 1부터 시작한다.
        
        queue = collections.deque([root])
        index = 2

        while queue:
            node = queue.popleft()
            if nodes[index] != '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
        
            if nodes[index] != '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root


if __name__ == '__main__':
    sol = Codec()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    codec = Codec()
    res = codec.serialize(root)
    deres = codec.deserialize(res)
    rres = codec.serialize(deres)
    print(res)
    print(deres)
    print(rres)
    