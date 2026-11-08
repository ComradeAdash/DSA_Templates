'''

DFS 

O(m + n)

O(n) space

'''

# DFS uses stack functionality through recursion to determine what to explore next
# searches vertically first
def dfs(graph, start):
    visited = set()
    traversal = []

    # explore pushes onto the call stack each time its called! This is our DFS stack
    def explore(node):
        if node in visited:
            return 

        visited.add(node)
        traversal.append(node)

        for neighbour in graph[node]:
            explore(neighbour)

        # node is popped, go to next node

    explore(start)

    return traversal