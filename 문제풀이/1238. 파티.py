"""
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3

오는거리는 알수있음. X부터 다익스트라 돌리면 되니깐
가는거리는?

1 = 가는데 4 오는데 1 = 5
3 = 가는데 6 오는데 3 = 9
4 = 가는데 3 오는데 7 = 10

"""

# import heapq
# import sys


# def dijkstra(start, graph):
#     distance = [float("inf")] * (len(graph) + 1)
#     distance[start] = 0

#     pq = [(0, start)]

#     while pq:
#         cost, v = heapq.heappop(pq)

#         if distance[v] < cost:
#             continue

#         for nc, nv in graph[v]:
#             new_cost = nc + cost
#             if new_cost < distance[nv]:
#                 distance[nv] = new_cost
#                 heapq.heappush(pq, (new_cost, nv))

#     return distance


# V, E, P = map(int, sys.stdin.readline().split())
# graph = {}
# for i in range(1, V + 1):
#     graph[i] = []

# for _ in range(E):
#     v1, v2, cost = map(int, sys.stdin.readline().split())
#     graph[v1].append((cost, v2))

# ans = [0] * (V + 1)
# back = dijkstra(P, graph)

# for i in range(1, V + 1):
#     go = dijkstra(i, graph)
#     ans[i] = go[P] + back[i]


# print(max(ans))

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
graph_rev = {}
for i in range(1, V + 1):
    graph[i] = []
    graph_rev[i] = []

for _ in range(E):
    v1, v2, cost = map(int, sys.stdin.readline().split())
    graph[v1].append((cost, v2))
    graph_rev[v2].append((cost, v1))

ans = [0] * (V + 1)
back = dijkstra(P, graph)
go = dijkstra(P, graph_rev)


print(max(go[i] + back[i] for i in range(1, V + 1)))
