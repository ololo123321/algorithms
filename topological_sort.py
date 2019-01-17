def topological_sort(g, v):
    # здесь нужна проверка на наличие циклов
    trace = []
    sorted_nodes = []

    def dfs(v):
        trace.append(v)
        children = g[v]
        if not children:
            sorted_nodes.extend(trace)
            trace.clear()
        for child in children:
            if child not in sorted_nodes:
                dfs(child)
    dfs(v)
    return sorted_nodes
