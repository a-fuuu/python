class MyCircularQueue:
    def __init__(self, x):
        self.q = [None] * x
        self.max = x
        self.p1 = 0
        self.p2 = 0
    
    def enQueue(self, value:int) -> bool:
        if self.q[self.p2]is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.max
            return True
        else:
            return False
    
    def deQueue(self):
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.max
            return True
    
    def Front(self):
        return -1 if self.q[self.p1] is None else self.q[self.p1]
    
    def Rear(self):
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]
    
    def isEmpty(self):
        return self.p1 == self.p2 and self.q[self.p1] is None
    
    def isFull(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None


if __name__ == '__main__':
    myqueue = MyCircularQueue(5)

    myqueue.enQueue(1)
    myqueue.enQueue(2)
    myqueue.enQueue(3)
    myqueue.enQueue(4)
    myqueue.enQueue(5)

    print(myqueue.deQueue())
    print(myqueue.deQueue())

    myqueue.enQueue(6)
    myqueue.enQueue(7)

    print(myqueue.Front())
    print(myqueue.Rear())