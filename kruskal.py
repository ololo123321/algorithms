def kruskal(edges, n_nodes):
    """
    Алгоритм Крускала поиска минимального остновного дерева.
    Релизован через систему непересекающихся множеств.
    Псевдокод:
    min_span_tree = []
    для каждого ребра (u,v) в сортированных по весу рёбрах графа:
        если u,v принадлежат одной компоненте связности:
            добавить (u,v) в min_span_tree
    """
    A = []
    parent = [0] * n_nodes  # массив предков
    size = [0] * n_nodes  # массив числа узлов в деревьях

    def find_set(x):
        """
        Поиск лидера множества (корня дерева) с использованием эвристики сжатия пути
        """
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for v in range(n_nodes):
        parent[v] = v
        size[v] = 1
    for u, v, _ in sorted(edges, key=lambda x: x[-1]):
        a, b = find_set(u), find_set(v)
        if a != b:
            A.append((u, v))
            # эвристика объединения по рангу:
            a, b = (a, b) if size[a] > size[b] else (b, a)
            parent[b] = a  # к большему дереву "прицепляем" меньшее
            size[a] += size[b]
    return A
