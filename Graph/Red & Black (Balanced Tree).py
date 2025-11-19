class Node:
    def __init__(self, value, parent=None, color="Red"):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        self.color = color

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color="Black")
        self.root = self.NIL

    def insert(self, node):
        new_node = Node(node, color="Red")
        new_node.left = self.NIL
        new_node.right = self.NIL
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current

            if new_node.value < current.value:
                current = current.left
            elif new_node.value > current.value:
                current = current.right
            else:
                return

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        self._fix_insert(new_node)

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == "Red":
            parent = node.parent
            grandparent = self._get_grandparent(node)

            if parent == grandparent.left:
                uncle = self._get_uncle(node)

                if uncle.color == "Red":
                    parent.color = "Black"
                    uncle.color = "Black"
                    grandparent.color = "Red"
                    node = grandparent
                elif node == parent.right:
                    node = parent
                    self._rotate_left(node)
                else:
                    parent.color = "Black"
                    grandparent.color = "Red"
                    self._rotate_right(grandparent)

            else:
                uncle = self._get_uncle(node)

                if uncle.color == "Red":
                    parent.color = "Black"
                    uncle.color = "Black"
                    grandparent.color = "Red"
                    node = grandparent
                elif node == parent.left:
                    node = parent
                    self._rotate_right(node)
                else:
                    parent.color = "Black"
                    grandparent.color = "Red"
                    self._rotate_left(grandparent)

        self.root.color = "Black"

    def remove(self, value):
        node = self.search(value)

        if node == self.NIL:
            return

        y = node
        y_original_color = y.color

        if node.left == self.NIL:
            x = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self._transplant(node, node.left)

        else:
            y = self._minimum(node.right)
            y_original_color = y.color
            x = y.right

            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if y_original_color == "Black":
            self._fix_remove(x)

    def _fix_remove(self, node):
        while node != self.root and node.color == "Black":
            parent = node.parent

            if node == parent.left:
                s = parent.right

                if s.color == "Red":
                    s.color = "Black"
                    parent.color = "Red"
                    self._rotate_left(parent)
                    s = parent.right
                elif s.left.color == "Black" and s.right.color == "Black":
                    s.color = "Red"
                    node = parent

                else:
                    if s.right.color == "Black":
                        s.left.color = "Black"
                        s.color = "Red"
                        self._rotate_right(s)
                        s = parent.right
                    s.color = parent.color
                    parent.color = "Black"
                    s.right.color = "Black"
                    self._rotate_left(parent)
                    node = self.root

            else:
                s = parent.left

                if s.color == "Red":
                    s.color = "Black"
                    parent.color = "Red"
                    self._rotate_right(parent)
                    s = parent.left
                elif s.right.color == "Black" and s.left.color == "Black":
                    s.color = "Red"
                    node = parent

                else:
                    if s.left.color == "Black":
                        s.right.color = "Black"
                        s.color = "Red"
                        self._rotate_left(s)
                        s = parent.left
                    s.color = parent.color
                    parent.color = "Black"
                    s.left.color = "Black"
                    self._rotate_right(parent)
                    node = self.root

        node.color = "Black"

    def search(self, value):
        current = self.root

        while current != self.NIL:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return None

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent

        if x.parent is None:
            self.root = y

        elif x == x.parent.left:
            x.parent.left = y

        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent

        if x.parent is None:
            self.root = y

        elif x == x.parent.right:
            x.parent.right = y

        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def _minimum(self, node):
        current = node

        while current.left != self.NIL:
            current = current.left
        return current

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _get_grandparent(self, node):
        if node is not None and node.parent is not None:
            return node.parent.parent
        return None

    def _get_uncle(self, node):
        grandparent = self._get_grandparent(node)

        if grandparent is None:
            return None
        if node.parent == grandparent.right:
            return grandparent.left
        return grandparent.right

    def _get_sibling(self, node):
        if node is None or node.parent is None:
            return None
        if node == node.parent.left:
            return node.parent.right
        return node.parent.left


# # # # # # # # # # # # # # #

rbt = RedBlackTree()
rbt.insert(10)
rbt.insert(85)
rbt.insert(15)
rbt.insert(70)
rbt.insert(20)
rbt.insert(60)
rbt.insert(30)
rbt.insert(50)
rbt.insert(65)
rbt.insert(80)
rbt.insert(90)
rbt.insert(40)
rbt.insert(5)
rbt.insert(55)

# # # # # # # # # # # # # # #

# rbt.remove(5)
# rbt.remove(85)
# rbt.remove(65)
# rbt.remove(70)
# rbt.remove(20)
# rbt.remove(60)
# rbt.remove(85)

# # # # # # # # # # # # # # #

print(rbt)


