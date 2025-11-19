class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.root = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        current_node = self.root

        if not self.root:
            self.root = new_node
            self.tail = new_node
            return

        if value < self.root.value:
            new_node.next = self.root
            self.root.prev = new_node
            new_node = self.root
            return

        while current_node.next and current_node.next.value < value:
            current_node = current_node.next

        new_node.next = current_node.next
        new_node.prev = current_node
        current_node.next = new_node

        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node

    def output(self):
        current_node = self.root

        if not self.root:
            return None

        print(f"ROOT -> ({self.root.value})")
        print(f"TAIL -> ({self.tail.value})")
        print("None <- ", end="")
        while current_node:
            print(f"[{current_node.value}]", end=" <-> ")
            current_node = current_node.next
        print("None")

    def search(self, target):
        current_node = self.root

        if not self.root:
            return None

        while current_node:
            if current_node.value == target:
                return True
            current_node = current_node.next
        return False

    def pop(self):
        pop_node = self.tail.value

        if not self.tail:
            return None

        if self.tail == self.root:
            self.root = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return pop_node

    def is_empty(self):
        if self.root:
            return False
        return True

    def qsize(self):
        current_node = self.root
        counter = 0

        if not self.root:
            return None

        while current_node:
            current_node = current_node.next
            counter += 1
        return counter

    def index(self, target):
        current_node = self.root
        counter = 0

        if not current_node:
            return None

        while current_node:
            if current_node.value == target:
                return counter
            current_node = current_node.next
            counter += 1
        return None

    def slice(self, start: int, stop: int):
        current_node = self.root
        temp = []
        counter = 0

        while current_node and counter < stop:
            if counter >= start:
                temp.append(current_node.value)
            current_node = current_node.next
            counter += 1
        return temp

    def insert(self, value):
        new_node = Node(value)
        current_node = self.root

        if not self.root:
            self.root = new_node
            self.tail = new_node
            return

        if value < self.root.value:
            new_node.next = self.root
            self.root.prev = new_node
            self.root = new_node
            return

        while current_node.next and current_node.next.value < value:
            current_node = current_node.next

        new_node.next = current_node.next
        new_node.prev = current_node
        current_node.next = new_node

        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node

ls = LinkedList()
ls.append(10)
ls.append(20)
ls.append(30)
ls.insert(100)
ls.insert(40)
ls.insert(0)

ls.output()




