import sys


def floyd(n, edges):
    INF = float("inf")
    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dist[i][i] = 0  # 자신으로 가는것 0

    for a, b, cost in edges:
        dist[a][b] = min(dist[a][b], cost)

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] == INF:
                dist[i][j] = 0
    return dist


V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

graph = {}

for i in range(1, V + 1):
    graph[i] = []

edges = []
for _ in range(E):
    edge = list(map(int, sys.stdin.readline().split()))
    edges.append(edge)

ans = floyd(V, edges)

for i in ans[1:]:
    print(*i[1:])
