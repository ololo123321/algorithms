def depth_first_search(g, v):
    """
    g - list, список смежности
    v - int, стартовая вершина
    """
    visited = []

    def dfs(v):
        visited.append(v)
        for child in g[v]:
            if child not in visited:
                dfs(child)
    dfs(v)
    return visited
