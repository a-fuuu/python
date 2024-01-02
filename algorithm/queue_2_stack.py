class Queue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def isEmpty(self):
        return not(bool(self.in_stack) or bool(self.out_stack))

    def transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def enqueue(self, item):
        return self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            self.transfer()
        if not self.isEmpty():
            return self.out_stack.pop()
        else:
            print("Queue is empty!")

    def __repr__(self):
        tmp = []
        tmp += self.out_stack[::-1]
        tmp += self.in_stack
        if tmp:
            return repr(tmp)
        else:
            return "Queue is empty!"