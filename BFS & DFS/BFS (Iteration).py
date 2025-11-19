from collections import deque

# BFS - Breadth First Search (Iteration)
#          A
#         / \
#        /   \
#       B     C
#      /     / \
#     D     E   F

graph_1 = {                                         # graph_1 - Это структура нашего графа.
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E", "F"],
    "D": ["B"],
    "E": ["C"],
    "F": ["F"]
}

def bfs(graph: dict, start: str):                   # Принимаем наш список - graph | и start - вершина с которой начнем.

    visited = set()                                 # Создаем множество что-бы хранить там пройденные вершины.
    dq = deque([start])                             # Создаем очередь (deque) и добавляем стартовую вершину в неё.

    while dq:                                       # Пока в очереди есть вершины.
        node = dq.popleft()                         # Берём первую(левую) вершину из нашего списка и -->

        if node not in visited:                     # Если вершины нет в множестве -->
            print(node)                             # Выводим вершину которой еще нет в списке.
            visited.add(node)                       # Добавляем вершину в список - "visited".
            print(visited)                          # Выводим весь список уже добавленных вершин.

            for neighbor in graph[node]:            # Для значения (values) в нашем графе под индексом[вершины которую мы взяли из очереди]
                if neighbor not in visited:         # Если значение не в списке - "visited", то -->
                    dq.append(neighbor)             # Добавляем значение в очередь.

bfs(graph=graph_1, start="A")                       # Вызываем функцию.





















