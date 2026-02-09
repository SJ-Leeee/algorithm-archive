"""
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

프림을 한바퀴돌리고 끊어버리는게 나을듯
"""

import heapq
import sys


def prim(graph, n, start=1):
    visited = [False] * (n + 1)

    pq = [(0, start)]
    vertex_count = 0
    total_count = 0

    max_cost = 0

    while pq and vertex_count < n:
        cost, v = heapq.heappop(pq)

        if visited[v]:
            continue

        max_cost = max(max_cost, cost)
        visited[v] = True
        total_count += cost
        vertex_count += 1

        for n_cost, n_v in graph[v]:
            if not visited[n_v]:
                heapq.heappush(pq, (n_cost, n_v))

    if vertex_count < n:
        return False

    return total_count - max_cost


V, E = map(int, sys.stdin.readline().split())
graph = {}
for i in range(1, V + 1):
    graph[i] = []

for _ in range(E):
    v1, v2, cost = map(int, sys.stdin.readline().split())
    graph[v1].append((cost, v2))
    graph[v2].append((cost, v1))

ans = prim(graph, V, 1)
print(ans)
