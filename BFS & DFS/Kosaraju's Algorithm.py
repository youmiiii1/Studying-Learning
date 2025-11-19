graph_1 = {
    "0": ["7"],
    "1": ["9"],
    "2": ["9", "10"],
    "3": ["8"],
    "4": ["2"],
    "5": ["3", "10"],
    "6": ["0", "1", "4"],
    "7": ["1", "6"],
    "8": ["5"],
    "9": ["4"],
    "10": ["8"],
    "11": ["2", "9", "5"]
}

def dfs_post_order(graph: dict, node: str, stack: list, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs_post_order(graph=graph, node=neighbour, stack=stack, visited=visited)
                
        stack.append(node)

def dfs_collect(graph: dict, node: str, visited, component):
    visited.add(node)
    component.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_collect(graph, neighbor, visited, component)

def kosaraju(graph: dict):
    visited = set()
    stack = []

    for node in graph:
        if node not in visited:
            dfs_post_order(graph, node, stack, visited)

    rev_graph = {node: [] for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            rev_graph[neighbor].append(node)

    visited = set()
    sccs = []

    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs_collect(rev_graph, node, visited, component)
            sccs.append(component)

    for num, item in enumerate(sccs, start=1):
        print(f"{num} - {item}")

kosaraju(graph_1)