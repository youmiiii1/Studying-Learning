class Stack:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

s = Stack()
s.append("1")
s.append("2")
s.append("3")
print(s.pop())
print(s.pop())
print(s.pop())
print(s.items)
print(s.is_empty())


