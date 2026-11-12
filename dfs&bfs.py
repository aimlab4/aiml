
## BFS 
# from collections import deque

# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])

#     while queue:
#         node = queue.popleft()

#         if node not in visited:
#             print(node, end=" ")
#             visited.add(node)

#             for neighbour in graph[node]:
#                 if neighbour not in visited:
#                     queue.append(neighbour)


# # Test Case 1: Connected Graph
# graph1 = {
#     0: [1], 1: [0, 2],
#     2: [1, 3], 3: [2]
# }

# # Test Case 2: Multiple Branches
# graph2 = {
#     0: [1, 2, 3],
#     1: [0], 2: [0, 4, 5],
#     3: [0], 4: [2], 5: [2]
# }

# # Test Case 3: Cyclic Graph
# graph3 = {
#     0: [1, 2], 1: [0, 2, 3],
#     2: [0, 1, 3], 3: [1, 2]
# }

# # Test Case 4: Single Node
# graph4 = {0: []}

# # Test Case 5: Disconnected Graph
# graph5 = {
#     0: [1], 1: [0],
#     2: [3], 3: [2]
# }

# bfs(graph2,1)

## DFS


def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)


# Test Case 1: Connected Graph
graph1 = {
    0: [1], 1: [0, 2],
    2: [1, 3], 3: [2]
}

# Test Case 2: Multiple Branches
graph2 = {
    0: [1, 2, 3],
    1: [0], 2: [0, 4, 5],
    3: [0], 4: [2], 5: [2]
}

# Test Case 3: Cyclic Graph
graph3 = {
    0: [1, 2], 1: [0, 2, 3],
    2: [0, 1, 3], 3: [1, 2]
}

# Test Case 4: Single Node
graph4 = {0: []}

# Test Case 5: Disconnected Graph
graph5 = {
    0: [1], 1: [0],
    2: [3], 3: [2]
}

dfs(graph1,1,set())

