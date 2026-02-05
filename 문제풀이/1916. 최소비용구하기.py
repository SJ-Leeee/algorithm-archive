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


def dijkstra(start, graph):
    dist = [float("inf")] * (len(graph) + 1)
    dist[start] = 0
    heap = [(start, 0)]

    while heap:
        v, cost = heapq.heappop(heap)

        if cost > dist[v]:
            continue

        for nv, nc in graph[v]:
            if nc + cost < dist[nv]:
                dist[nv] = nc + cost
                heapq.heappush(heap, (nv, nc + cost))

    return dist


V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
graph = {}
for i in range(1, V + 1):
    graph[i] = []
for _ in range(E):
    v1, v2, cost = map(int, sys.stdin.readline().split())
    graph[v1].append((v2, cost))

start, end = map(int, sys.stdin.readline().split())
dist = dijkstra(start, graph)

print(dist[end])
