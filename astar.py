
def astar(graph, heuristic, start, goal):
    open_list = [start]
    cost = {start: 0}
    parent = {}

    while open_list:
        current = min(open_list,
                      key=lambda n: cost[n] + heuristic[n])

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            print("Path:", path[::-1])
            print("Cost:", cost[goal])
            return

        open_list.remove(current)

        for neighbour, weight in graph[current]:
            new_cost = cost[current] + weight

            if neighbour not in cost or new_cost < cost[neighbour]:
                cost[neighbour] = new_cost
                parent[neighbour] = current

                if neighbour not in open_list:
                    open_list.append(neighbour)

    print("No path found")


# Sample Test Case
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 5)],
    'E': [('G', 3)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'G': 0
}

astar(graph, heuristic, 'A', 'G')
