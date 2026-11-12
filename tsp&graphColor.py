
from itertools import permutations

def tsp(graph, start):
    cities = list(graph.keys())
    cities.remove(start)

    min_cost = float('inf')
    best_path = []

    for path in permutations(cities):
        route = [start] + list(path) + [start]
        cost = 0

        for i in range(len(route) - 1):
            cost += graph[route[i]][route[i + 1]]

        if cost < min_cost:
            min_cost = cost
            best_path = route

    print("Shortest Path:", best_path)
    print("Minimum Cost:", min_cost)


# Sample Test Case
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

tsp(graph, 'A')



## GRAPH COLORING


def is_safe(graph, colors, node, color):
    for neighbour in range(len(graph)):
        if graph[node][neighbour] == 1 and colors[neighbour] == color:
            return False
    return True


def graph_coloring(graph, m, colors, node):
    if node == len(graph):
        return True

    for color in range(1, m + 1):
        if is_safe(graph, colors, node, color):
            colors[node] = color

            if graph_coloring(graph, m, colors, node + 1):
                return True

            colors[node] = 0

    return False


# Sample Test Case
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

m = 3
colors = [0] * len(graph)

if graph_coloring(graph, m, colors, 0):
    print("Color Assignment:")
    for i in range(len(colors)):
        print("Node", i, ":", "Color", colors[i])
else:
    print("No solution exists")

