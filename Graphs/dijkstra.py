'''

Dijkstra's

Slow: O(mn)
Fast with Priority Queue: O(m)

'''

import heapq

def dijkstra(graph, start):
    n = len(graph)

    distances = [float("inf")] * n
    distances[start] = 0

    min_heap = [(0, start)]

    while min_heap:
        cost, node = heapq.heappop(min_heap)

        if cost > distances[node]:
            continue

        for neighbour, weight in graph[node]:
            new_cost = cost + weight

            if new_cost < distances[neighbour]:
                distances[neighbour] = new_cost

                heapq.heappush(min_heap,(new_cost,neighbour))

    return distances