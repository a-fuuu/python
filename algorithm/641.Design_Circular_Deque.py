class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class MyCircularDeque:
    def __init__(self, x):
        self.max_size = x
        self.size = 0
        self.front = Node(None)
        self.rear = Node(None)
        self.front.next = self.rear
        self.rear.prev = self.front

    def insertFront(self, data):
        if self.size == self.max_size:
            return False
        node = Node(data)
        node.next = self.front.next
        node.prev = self.front
        self.front.next.prev = node
        self.front.next = node
        self.size += 1
        return True
    
    def insertLast(self, data):
        if self.size == self.max_size:
            return False
        node = Node(data)
        node.next = self.rear
        node.prev = self.rear.prev
        self.rear.prev.next = node
        self.rear.prev = node
        self.size += 1
        return True
    
    def deletefront(self):
        if self.size == 0:
            return False
        self.front.next.next.prev = self.front
        self.front.next = self.front.next.next
        self.size -= 1
        return True
    
    def deleteLast(self):
        if self.size == 0:
            return False
        self.rear.prev.prev.next = self.rear
        self.rear.prev = self.rear.prev.prev
        self.size -= 1
        return True
    
    def getFront(self):
        return self.front.next.value if self.size != 0 else -1

    def getRear(self):
        return self.rear.prev.value if self.size != 0 else -1

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity