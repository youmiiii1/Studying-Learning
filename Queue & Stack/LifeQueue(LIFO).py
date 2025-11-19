from queue import LifoQueue

class Stack:
    def __init__(self):
        self.items = LifoQueue()

    def put(self, item):
        self.items.put(item)

    def get(self):
        return self.items.get()

    def empty(self):
        return self.items.empty()

    def qsize(self):
        return self.items.qsize()

s = Stack()
s.put("Apple")
s.put("Orange")
print(s.qsize())
print(s.get())
print(s.get())
print(s.empty())