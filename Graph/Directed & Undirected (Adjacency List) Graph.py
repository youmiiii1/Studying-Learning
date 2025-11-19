class Node:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_neighbor(self, nbr, weight=0):
        self.edges[nbr] = weight

    def __repr__(self):
        edges_str = ", ".join(f"{nbr.value}({w})" for nbr, w in self.edges.items())
        return f"{self.value} -> {edges_str}"

class Graph:
    def __init__(self, is_directed=False):
        self.is_directed = is_directed
        self.graph = {}
        self.count_node = 0
        self.count_edges = 0

    def add_node(self, value):
        if value not in self.graph:
            new_node = Node(value)
            self.graph[value] = new_node
            self.count_node += 1

    def add_edge(self, node_from, node_to, weight=0):
        if not node_from in self.graph:
            self.add_node(node_from)

        if not node_to in self.graph:
            self.add_node(node_to)

        self.graph[node_from].add_neighbor(self.graph[node_to], weight)
        self.count_edges += 1

        if not self.is_directed:
            self.graph[node_to].add_neighbor(self.graph[node_from], weight)
            self.count_edges += 1

    def remove_node(self, value):
        if not value in self.graph:
            return None

        node_to_remove = self.graph[value]
        outgoing_edges_count = len(node_to_remove.edges)

        for node in self.graph.values():
            if node_to_remove in node.edges:
                del node.edges[node_to_remove]
                self.count_edges -= 1

        self.count_edges -= outgoing_edges_count

        del self.graph[value]
        self.count_node -= 1

        return None

    def remove_edge(self, edge_from, edge_to):
        if edge_from not in self.graph or edge_to not in self.graph:
            return None

        from_node = self.graph[edge_from]
        to_node = self.graph[edge_to]

        if to_node in from_node.edges:
            del from_node.edges[to_node]
            self.count_edges -= 1

        if not self.is_directed:
            if from_node in to_node.edges:
                del to_node.edges[from_node]
                self.count_edges -= 1

        return None

    def has_edge(self, node_1, node_2):
        if node_1 not in self.graph or node_2 not in self.graph:
            return False

        if self.graph[node_2] in self.graph[node_1].edges:
            return True
        return False

    def get_neighbors(self, node):
        if node not in self.graph:
            return None
        else:
            current_node = self.graph[node]
            neighbours_str = ", ".join([f"{nbr.value}({weight})" for nbr, weight in current_node.edges.items()])
            return f"Neighbors of node ({current_node.value}) is: {neighbours_str}"

    def count_nodes_and_edges(self):
        return f"Node's in graph: {self.count_node} | Edge's in graph: {self.count_edges}"

    def clear(self):
        self.graph = {}
        self.count_node = 0
        self.count_edges = 0

    def get_graph(self):
        for node in self.graph.values():
            print(node)

g = Graph(is_directed=False)
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")

g.add_edge("A", "B")
g.add_edge("D", "E")

print(g.count_nodes_and_edges())
g.get_graph()