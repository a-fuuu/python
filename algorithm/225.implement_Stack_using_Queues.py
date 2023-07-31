# 큐(Queue)를 활용하여 스택을 구현하시오

import collections

class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)

        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]
    
    def empty(self):
        return len(self.q) == 0
    

if __name__ == '__main__':
    mystack = MyStack()

    mystack.push(1)
    mystack.push(2)
    mystack.push(3)
    mystack.push(4)
    mystack.push(5)

    print(mystack.pop())
    print(mystack.pop())
    print(mystack.pop())
    print(mystack.pop())
    print(mystack.pop())

    print(mystack.empty())