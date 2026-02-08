import sys


def floyd(n, edges):
    INF = float("inf")
    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    for a, b, cost in edges:
        dist[a][b] = min(dist[a][b], cost)

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


V, E = map(int, sys.stdin.readline().split())
edges = []

for _ in range(E):
    edge = list(map(int, sys.stdin.readline().split()))
    edges.append(edge)

INF = float("inf")
ret = floyd(V, edges)
ans = INF

for i in range(1, V + 1):
    ans = min(ans, ret[i][i])

print(ans if ans != INF else -1)