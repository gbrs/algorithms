"""
BFS: обход графа в ширину
"""


from collections import deque


def bfs(graph: dict) -> list:
    # создаем список для посещенных вершин,
    # очередь для будущего посещения
    # и список последовательности обхода
    visited_nodes = set()
    queue = deque()
    path = []

    START_NODE = 1

    visited_nodes.add(START_NODE)
    queue.append(START_NODE)

    while queue:
        # пока очередь непустая
        # обрабатываем левую вершину очереди (explored_node):
        # печатаем ее, попаем и добавляем всех ее соседок в очередь
        explored_node = queue.popleft()
        path.append(explored_node)

        for neighbor in graph[explored_node]:
            if neighbor not in visited_nodes:
                visited_nodes.add(neighbor)
                queue.append(neighbor)

    return path


if __name__ == '__main__':

    # описываем граф, используя списки смежности
    GRAPH = {
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

    '''GRAPH = {
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

    print(*bfs(GRAPH), sep=' -> ')