import heapq
import sys


def dijkstra(start, graph):
    distance = [float("inf")] * (len(graph) + 1)
    distance[start] = 0

    pq = [(0, start)]

    while pq:
        cost, v = heapq.heappop(pq)
        if cost > distance[v]:
            continue

        for nv, nc in graph[v]:
            new_cost = nc + cost
            if new_cost < distance[nv]:
                distance[nv] = new_cost
                heapq.heappush(pq, (new_cost, nv))

    return distance


V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = {}

for i in range(1, V + 1):
    graph[i] = []

for _ in range(E):
    v1, v2, cost = map(int, sys.stdin.readline().split())
    graph[v1].append((v2, cost))

dist = dijkstra(start, graph)
for i in dist[1:]:
    if i == float("inf"):
        print("INF")
    else:
        print(i)
