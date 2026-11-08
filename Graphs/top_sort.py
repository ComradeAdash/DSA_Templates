'''

Topological Sort

O(m + n)

O(n) space

'''

from collections import deque

# removing nodes and noting incoming edge counts that drop, specifically ones that drop to 0
# counts that drop to 0 are added to our queue and removed from the graph

def top_sort(graph):
    n = len(graph)
    indegree = [0] * n

    for node in range(n):
        for neighbour in graph[node]:
            indegree[neighbour] += 1

    q = deque()

    for node in range(n):
        if indegree[node] == 0:
            q.append(node)

    order = []

    while q:
        node = q.popleft()
        order.append(node)

        for neighbour in graph[node]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                q.append(neighbour)

    # there is a cycle, gotta stop
    if len(order) != n:
        return []

    return order