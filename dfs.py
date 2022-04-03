"""
рекурсивный DFS. Прямой обход: NLR.
"""


def dfs(node):
    """
    рекурсивно обходим граф: NLR
    :param node: вершина, которую исследуем
    :return: None
    внешние эффекты: изменяем список visited_vertices
    """

    # если вершина уже посещена, выходим в предыдущий этап стека вызовов (шаг назад по дереву)
    if node in visited_nodes:
        return

    visited_nodes.append(node)  # записываем вершину в посещенные

    for neighbor in GRATH[node]:  # обходим все смежные вершины
        if neighbor not in visited_nodes:
            dfs(neighbor)  # рекурсивно проваливаясь в еще не посещенные


# описываем граф, используя списки смежности
GRATH = {
    1: [2, 3, 4],
    2: [1, 5, 6],
    3: [1],
    4: [1, 7, 8],
    5: [2, 9, 10],
    6: [2],
    7: [4, 11, 12],
    8: [4],
    9: [5],
    10: [5],
    11: [7],
    12: [7]
}
# https://lisiynos.github.io/s1/graph_alg/breadth-first-tree.png

'''graph = {
    1: [2, 8],
    2: [1, 3, 8],
    3: [2, 4, 8],
    4: [3, 7, 9],
    5: [6, 7],
    6: [5],
    7: [4, 5, 8],
    8: [1, 2, 3, 7],
    9: [4],
}
# https://lisiynos.github.io/s1/graph_alg/primer.gif
'''

# создаем список для посещенных вершин.
# А стек у нас создается за счет стека рекурсивных вызовов?
visited_nodes = []

START_NODE = 1
dfs(START_NODE)

print(*visited_nodes, sep=' -> ')
