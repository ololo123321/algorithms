from collections import deque


def breadth_first_search(g, v):
    """
    g - list, список смежности
    v - int, стартовая вершина
    """
    used = []
    queue = deque([v])  # FIFO
    visited = []  # посещённые вершины
    while queue:
        v = queue.popleft()
        visited.append(v)
        for child in g[v]:
            if child not in used + visited:  # случай цикла
                used.append(child)
                queue.append(child)
    return visited
