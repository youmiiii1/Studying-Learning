# DFS - Depth First search (Recursion)
#          A
#         / \
#        /   \
#       B     C
#      /     / \
#     D     E   F
#

graph_1 = {                                                     # graph_1 - Это структура нашего графа.
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E", "F"],
    "D": ["B"],
    "E": ["C"],
    "F": ["F"]
}



def dfs(graph: dict, node: str, visited=None):                  # Принимаем сам graph(Dict), Node(str | Вершина с которой мы будем начинать) -->
                                                                # и visited(=None | Что-бы просчитать были ли мы уже на этой вершине или нет.)

    if visited is None:                                         # Если это первый запуск (Значит что visited=None), то мы ->
        visited = set()                                         # Создаем множество что-бы хранить там пройденные вершины.
    print(f"Explore node {node} -> {node not in visited}")      # Показываем с какой вершины начинаем и показываем то-что эта вершина еще не в множестве "visited", то-есть мы по ней еще не прошли.

    if node not in visited:                                     # Если вершина еще не в множестве "visited"
        print(f"Visited - {node}")                              # Выводим текущую вершину и -->
        visited.add(node)                                       # Добавляем эту вершину в множество "visited"

        for neighbor in graph[node]:                            # Для каждого элемента(values) в графе[под индексом нашей взятой ноды.]
            dfs(graph=graph, node=neighbor, visited=visited)    # Вызываем функцию еще раз, graph=graph(Остаемся все еще в этом графе так-как работаем с ним) -->
                                                                # node=neighbor(Каждая следующая вершина), visited=visited(Каждый вызов функции передаем обновленный список.)

    return visited

print(dfs(graph_1, "A"))



