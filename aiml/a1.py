from collections import deque
def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])
    visited.append(start_node)
    print("BFS Traversal Sequence:")
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    print()
# Adjacency list based on the Q1 tree diagram
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8, 9],
    5: [10, 11],
    6: [12, 13],
    7: [14, 15],
    8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: []
}
bfs(graph, 1)