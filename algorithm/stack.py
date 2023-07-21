class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item

test_stack = Stack()

test_stack.push(1)
test_stack.push(2)
test_stack.push(3)
test_stack.push(4)
test_stack.push(5)

if __name__ == '__main__':
    while test_stack.last:
        print(test_stack.pop())