class Node: 
    def __init__(self, item):
        self.item = item
        self.next = None
class LinkedList:
    def __init__(self):
        self.front = None
        self.curr = None

    def empty(self):
        return self.front is None

    def reset(self):
        self.curr = self.front

    def next(self):
        if self.empty():
            raise StopIteration
        self.curr = self.curr.next

    def insert_after(self, item):
        node = Node(item)
        if self.empty():
            self.front = self.curr = node
            return
        node.next = self.curr.next
        self.curr.next = node
    def insert_before(self, item):
        node = Node(item)
        if self.empty():
            self.front = self.curr = node
            return
        if self.front is self.curr:
            node.next = self.front
            self.front = node
            self.curr=node
            return
        prev = self.front
        while prev.next is not self.curr:
            prev = prev.next
        node.next = self.curr
        prev.next = node
    def to_linkedList(self,str):
        self.insert_after(str[0])
        for i in range(1, len(str[1:]) + 1):
            if i != 1:
                self.next()
            self.insert_after(str[i])

        
    def current(self):
        if self.empty():
            raise RuntimeError
        return self.curr.item

    def print(self):
        self.reset()
        while self.curr!=None:
            print(self.curr.item,end = " ")
            self.next()
        self.reset()
        print()

    def PrintReverse(self):
        l = LinkedList()
        self.reset()
        i = 0
        while True:
            l.insert_before(self.curr.item)
            self.next()
            if self.curr is None:
                break
            i += 1
        l.print()

if __name__=="__main__":
    str = [1,2,3,4]
    l = LinkedList()
    l.to_linkedList(str)
    l.print()
    l.PrintReverse()
        
