def ford_bellman(n, s, edges):
    """
    Алгоритм Форда-Беллмана поиска кратчайшего расстояния от вершины s до остальных вершин графа
    n - число вершин
    s - номер стартовой вершины
    edges - массив рёбер графа
    """
    inf = 1e10
    dists = [inf] * n
    dists[s] = 0
    p = [0] * n
    for _ in range(n):
        for u, v, d in edges:
            d_new = dists[v] + d
            if d_new < dists[u]:
                p[u] = v
                dists[u] = d_new
    return dists, p


def ford_bellman_fast(n, s, edges):
    """
    Модификация алгоритма Форда-Беллмана.
    Алгоритм останавливается, если после итерации i ни одно расстояние не улучшилось
    """
    inf = 1e10
    dists = [inf] * n
    dists[s] = 0
    p = [0] * n
    for _ in range(n):
        flag = True
        for u, v, d in edges:
            d_prev = dists[u]
            d_new = dists[v] + d
            if d_new < d_prev:
                p[u] = v
                dists[u] = d_new
            if d_prev != d_new:
                flag = False
        if flag:
            return dists
    return dists
