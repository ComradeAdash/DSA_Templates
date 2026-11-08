'''

BFS

O(m + n)

O(n) space

'''

from collections import deque

# uses a queue to track nodes
# searches horizatonally first (the layers)
def bfs(graph, start):
    visited = {start}
    q = deque([start])
    traversal = []

    # while the queue is not empty we go
    while q: 
        node_to_visit = q.popleft()
        traversal.append(node_to_visit)

        for neighbour in graph[node_to_visit]:
            if neighbour not in visited:
                visited.add(neighbour)
                q.append(neighbour)

    return traversal

