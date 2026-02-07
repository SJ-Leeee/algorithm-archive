"""
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
"""

import heapq
import sys


def dijkstra_with_path(start, end, graph):
    INF = float("inf")
    distance = [INF] * (len(graph) + 1)
    parent = [-1] * (len(graph) + 1)
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        cost, v = heapq.heappop(pq)
        if cost > distance[v]:
            continue

        for nc, nv in graph[v]:
            new_cost = cost + nc
            if new_cost < distance[nv]:
                distance[nv] = new_cost
                parent[nv] = v
                heapq.heappush(pq, (new_cost, nv))

    path = []
    current = end
    while current != -1:
        path.append(current)
        current = parent[current]

    return distance[end], path[::-1]


V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
graph = {}
for i in range(1, V + 1):
    graph[i] = []

for _ in range(E):
    v1, v2, cost = map(int, sys.stdin.readline().split())
    graph[v1].append((cost, v2))

start, end = map(int, sys.stdin.readline().split())

dist, path = dijkstra_with_path(start, end, graph)
print(dist)
print(len(path))
print(*path)
