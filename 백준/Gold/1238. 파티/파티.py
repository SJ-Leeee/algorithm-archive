import heapq
import sys


def dijkstra(start, graph):
    distance = [float("inf")] * (len(graph) + 1)
    distance[start] = 0

    pq = [(0, start)]

    while pq:
        cost, v = heapq.heappop(pq)

        if distance[v] < cost:
            continue

        for nc, nv in graph[v]:
            new_cost = nc + cost
            if new_cost < distance[nv]:
                distance[nv] = new_cost
                heapq.heappush(pq, (new_cost, nv))

    return distance


V, E, P = map(int, sys.stdin.readline().split())
graph = {}
for i in range(1, V + 1):
    graph[i] = []

for _ in range(E):
    v1, v2, cost = map(int, sys.stdin.readline().split())
    graph[v1].append((cost, v2))

ans = [0] * (V + 1)
back = dijkstra(P, graph)

for i in range(1, V + 1):
    go = dijkstra(i, graph)
    ans[i] = go[P] + back[i]


print(max(ans))
