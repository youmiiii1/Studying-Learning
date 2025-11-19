class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self):
        return f"Node({self.value})"

class SearchBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    return

                else:
                    current = current.left

            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    return

                else:
                    current = current.right

            else:
                return

    def remove_predecessor(self, value):
        parent = None
        current = self.root

        while current and current.value != value:
            parent = current

            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current is None:
            return False

        if current.left is None:
            if parent is None:
                self.root = current.right
                if self.root:
                    self.root.parent = None

            elif parent.left == current:
                parent.left = current.right
                if current.right:
                    current.right.parent = parent

            else:
                parent.right = current.right
                if current.right:
                    current.right.parent = parent

            return True

        successor_parent = current
        successor = current.left

        while successor.right:
            successor_parent = successor
            successor = successor.right

        current.value = successor.value

        if successor_parent.left == successor:
            successor_parent.left = successor.left
            if successor.left:
                successor.left.parent = successor_parent

        else:
            successor_parent.right = successor.left
            if successor.left:
                successor.left.parent = successor_parent

        return True

    def remove_successor(self, value):
        parent = None
        current = self.root

        while current and current.value != value:
            parent = current

            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current is None:
            return False

        if current.right is None:
            if parent is None:
                self.root = current.left
                if self.root:
                    self.root.parent = None

            elif parent.left == current:
                parent.left = current.left
                if current.left:
                    current.left.parent = parent

            else:
                parent.right = current.left
                if current.left:
                    current.left.parent = parent

            return True

        successor_parent = current
        successor = current.right

        while successor.left:
            successor_parent = successor
            successor = successor.left

        current.value = successor.value

        if successor_parent.left == successor:
            successor_parent.left = successor.right
            if successor.right:
                successor.right.parent = successor_parent

        else:
            successor_parent.right = successor.right
            if successor.right:
                successor.right.parent = successor_parent

        return True

    def search(self, value):
        current = self.root

        while current:

            if value == current.value:
                return current

            elif value < current.value:
                current = current.left

            else:
                current = current.right

        return None

# # # # # # # # # #

bst = SearchBinaryTree()

bst.insert(42)
bst.insert(17)
bst.insert(68)
bst.insert(3)
bst.insert(20)
bst.insert(50)
bst.insert(99)
bst.insert(15)
bst.insert(25)
bst.insert(60)
bst.insert(75)
bst.insert(5)
bst.insert(1)
bst.insert(88)
bst.insert(100)

bst.remove_predecessor(60)
bst.remove_predecessor(17)
bst.remove_predecessor(5)
bst.remove_predecessor(68)
bst.remove_predecessor(42)