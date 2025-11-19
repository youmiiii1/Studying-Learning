from collections import deque

class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def is_leaf(self):
        return self.left is None and self.right is None

    def get_parent(self):
        return self.parent

    def get_depth(self):
        depth = 0
        current = self

        while current.parent is not None:
            depth += 1
            current = current.parent
        return depth

    def __repr__(self):
        return f"Node({self.value})"

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            if node.left is None:
                node.left = new_node
                new_node.parent = node
                return

            else:
                queue.append(node.left)

            if node.right is None:
                node.right = new_node
                new_node.parent = node
                return

            else:
                queue.append(node.right)

    def remove(self, value):
        if self.root is None:
            return False

        node_to_delete = None
        last_node = None
        queue = deque([self.root])

        while queue:
            last_node = queue.popleft()

            if last_node.value == value:
                node_to_delete = last_node

            if last_node.left:
                queue.append(last_node.left)

            if last_node.right:
                queue.append(last_node.right)

        if node_to_delete is None:
            return False

        if node_to_delete == self.root and not self.root.left and not self.root.right:
            self.root = None
            return True

        if node_to_delete == last_node:
            if last_node.parent:
                if last_node.parent.right == last_node:
                    last_node.parent.right = None
                else:
                    last_node.parent.left = None
            else:
                self.root = None

            return True

        node_to_delete.value = last_node.value

        if last_node.parent:
            if last_node.parent.right == last_node:
                last_node.parent.right = None
            else:
                last_node.parent.left = None
        else:
            self.root = None

        return True

    def search(self,value):
        if self.root is None:
            return None

        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            if node.value == value:
                return node

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return None

    def traverse(self, method="level_order"):
        result = []

        if self.root is None:
            return result

        if method == "pre_order":
            self._pre_order(self.root, result)

        elif method == "in_order":
            self._in_order(self.root, result)

        elif method == "post_order":
            self._post_order(self.root, result)

        elif method == "level_order":
            queue = deque([self.root])

            while queue:
                node = queue.popleft()
                result.append(node.value)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result

    def _pre_order(self, node, result):
        if not node:
            return

        result.append(node.value)
        self._pre_order(node.left, result)
        self._pre_order(node.right, result)

    def _in_order(self, node, result):
        if not node:
            return

        self._in_order(node.left, result)
        result.append(node.value)
        self._in_order(node.right, result)

    def _post_order(self, node, result):
        if not node:
            return

        self._post_order(node.left, result)
        self._post_order(node.right, result)
        result.append(node.value)

    def get_height(self):
        if self.root is None:
            return -1

        height = -1
        queue = deque([self.root])

        while queue:
            height += 1

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
        return height

    def get_path(self, value):
        node = self.search(value)

        if not node:
            return []

        path = []
        current_node = node

        while current_node is not None:
            path.append(current_node.value)
            current_node = current_node.parent

        return path[::-1]

    def get_root(self):
        return self.root

    def get_leaves(self):
        if self.root is None:
            raise ValueError("Tree empty.")

        leaves = []
        queue = deque([self.root])

        while queue:
            node =  queue.popleft()

            if node.is_leaf():
                leaves.append(node)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return leaves

# # # # # # # # # #

bt = BinaryTree()

bt.insert(42)
bt.insert(17)
bt.insert(68)
bt.insert(3)
bt.insert(20)
bt.insert(50)
bt.insert(99)
bt.insert(15)
bt.insert(25)
bt.insert(60)
bt.insert(75)
bt.insert(5)
bt.insert(1)
bt.insert(88)
bt.insert(100)

# bt.remove(15)
# bt.remove(25)
# bt.remove(23)

# # # # # # # # # #

test_node = bt.search(25)
if test_node is None:
    print("Node not found.")
else:
    print(f"Leaf: {test_node.is_leaf()}")

# # # # # # # # # #

test_node_1 = bt.search(25)
if test_node_1 is None:
    print("Node not found.")
else:
    print(f"Depth: {test_node_1.get_depth()}")

# # # # # # # # # #

test_node_2 = bt.search(5)
if test_node_2 is None:
    print("Node not found.")
else:
    print(f"Parent: {test_node_2.get_parent()}")

# # # # # # # # # #

print(f"Root: {bt.get_root()}")
print(f"Get path: {bt.get_path(25)}")
print(f"Search: {bt.search(25)}")
print(f"Leaves: {bt.get_leaves()}")
print(f"Height: {bt.get_height()}")

# # # # # # # # # #

print(f"Level Order: {bt.traverse('level_order')}")
print(f"Post Order: {bt.traverse('post_order')}")
print(f"In Order: {bt.traverse('in_order')}")
print(f"Pre Order: {bt.traverse('pre_order')}")

# # # # # # # # # #