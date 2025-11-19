from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()

    def append(self, item):
        self.items.append(item)

    def append_left(self, item):
        self.items.appendleft(item)

    def pop(self):
        return self.items.pop()

    def pop_left(self):
        return self.items.popleft()

s = Stack()
s.append("Orange")
s.append_left("Apple")
print(s.items)
print(s.pop())
print(s.pop_left())



