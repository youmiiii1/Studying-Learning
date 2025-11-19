from queue import PriorityQueue

class Stack:
    def __init__(self):
        self.items = PriorityQueue()

    def put(self, priority, item):
        self.items.put((priority, item))

    def get(self):
        return self.items.get()

    def empty(self):
        return self.items.empty()

    def qsize(self):
        return self.items.qsize()

s = Stack()
s.put(1, "Apple")
s.put(3, "Orange")
s.put(2, "Banana")
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())
print(s.empty())
