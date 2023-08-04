import collections

class ListNode:
    def __init__(self, key = None, value = int):
        self.key = key
        self.value = value
        self.next = None

class MyhashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key, value: int)->None:
        index = key % self.size

        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        p = self.table[index]

        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
    
    def get(self, key:int)-> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
    

    def remove(self, key:int)->None:
        index = key % self.size
        if self.table[index].value is None:
            return
        
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


if __name__ == '__main__':
    myhashmap = MyhashMap()
    print(myhashmap.put(1,1))
    print(myhashmap.put(2,2))
    print(myhashmap.get(1))
    print(myhashmap.get(3))
    print(myhashmap.put(2,1))
    print(myhashmap.remove(2))
    print(myhashmap.get(2))