from queue import Queue

class Stack:
    def __init__(self):
        self.items = Queue()

    def put(self, item):
        self.items.put(item)

    def get(self):
        return self.items.get()

    def empty(self):
        return self.items.empty()

    def qsize(self):
        return self.items.qsize()

s = Stack()
s.put("1")
s.put("2")
s.put("3")
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())
print(s.empty())
