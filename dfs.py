"""
рекурсивный DFS. Прямой - NLR.
"""


def dfs(vertica):
    """
    рекурсивно обходим граф
    :param vertica: вершина, которую исследуем
    :return: None
    внешние эффекты: изменяем список visited_vertices
    """

    # если вершина уже посещена, выходим в предыдущий этап стека вызовов (шаг назад по дереву)
    if vertica in visited_vertices:
        return

    visited_vertices.append(vertica)  # записываем вершину в посещенные

    for neighbor in graph[vertica]:  # обходим все смежные вершины
        if neighbor not in visited_vertices:
            dfs(neighbor)  # рекурсивно проваливаясь в еще не посещенные


# описываем граф, используя списки смежности
graph = {
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

# создаем список для посещенных вершин.
# А стек у нас создается за счет стека рекурсивных вызовов?
visited_vertices = []

start_vertica = 1
dfs(start_vertica)

print(visited_vertices)
