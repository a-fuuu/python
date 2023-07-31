# 스택을 활용하여 큐(Queue)를 구현하시오

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    # 왜 input ouput을 나누었는가?,,
    # queue의 pop은 stack과 다르니까 선입선출이니까

    def push(self, x):
        self.input.append(x)

    # pop method에서 peek를 불러오는 방식 
    # input을 output에 다 넣어놓고 하는 방식으로다가

    def pop(self):
        self.peek()
        return self.output.pop()
    
    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    
    def empty(self):
        return self.input == [] and self.output == []
    

if __name__ == '__main__':
    myqueue = MyQueue()

    myqueue.push(1)
    myqueue.push(2)
    myqueue.push(3)
    myqueue.push(4)
    myqueue.push(5)

    print(myqueue.pop())
    print(myqueue.pop())
    print(myqueue.pop())
    print(myqueue.pop())
    print(myqueue.pop())

    print(myqueue.empty())