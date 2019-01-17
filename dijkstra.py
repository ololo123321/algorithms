def dijkstra(g, s):
    """
    Алгоритм Дейсктры поиска кратчайшего расстояния от вершины s до остальных вершин графа
    Идея: на каждой из n итераций помечается одна вершина,
    причём расстояние до данной вершини от s является наименьшим
    и не меняется в дальнейшем
    g - граф, заданный массивом длины n из массивов пар (вершина, расстояние), где n - число вершин графа
    s - номер стартовой вершины
    """
    inf = 1e10
    n = len(g)
    u = [False] * n
    dists = [inf] * n
    dists[s] = 0
    p = [0] * n
    for _ in range(n):  # главный цикл. на каждой итерации помечается ровно одна вершина
        min_dist = inf
        v_best = 0
        for v in range(n):
            if dists[v] < min_dist and not u[v]:
                v_best = v
                min_dist = dists[v]
        dists[v_best] = min_dist
        u[v_best] = True
        for to, d in g[v_best]:
            d_new = dists[v_best] + d
            if d_new < dists[to]:
                p[to] = v_best
                dists[to] = d_new
    return dists, p


def get_path(start, end, p):
    """
    Функция восстановления маршрута из вершины start в вершину end с помощью массива предков p
    """
    path = []
    while end != start:
        path.append(end)
        end = p[end]
    path.append(start)
    return path[::-1]
