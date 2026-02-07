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


V, E = map(int, sys.stdin.readline().split())
graph = {}
for i in range(1, V + 1):
    graph[i] = []

for _ in range(E):
    v1, v2, cost = map(int, sys.stdin.readline().split())
    graph[v1].append((cost, v2))
    graph[v2].append((cost, v1))
ans = 0
stop1, stop2 = map(int, sys.stdin.readline().split())
dist_start = dijkstra(1, graph)
dist_stop1 = dijkstra(stop1, graph)
dist_stop2 = dijkstra(stop2, graph)

INF = float("inf")


case1 = dist_start[stop1] + dist_stop1[stop2] + dist_stop2[V]
case2 = dist_start[stop2] + dist_stop2[stop1] + dist_stop1[V]

if case1 == case2 == INF:
    print(-1)
elif case1 > case2:
    print(case2)
else:
    print(case1)

# 경우의 수 1 - s1 - s2 - N
# 경우의 수 1 - s2 - s1 - N
