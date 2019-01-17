from itertools import chain
from dfs import depth_first_search


def connected_components(g, v):
    nodes = set(chain(*g))
    components = []
    while nodes:
        comp = depth_first_search(g, v)
        components.append(comp)
        nodes -= set(comp)
        if nodes:
            v = list(nodes)[0]
    return components
