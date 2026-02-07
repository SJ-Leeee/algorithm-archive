import sys


def bellman_ford(n, start, edges):
    INF = float("inf")
    dist = [INF] * (n + 1)
    dist[start] = 0

    for _ in range(n - 1):
        for a, b, cost in edges:
            if dist[a] != INF and dist[a] + cost < dist[b]:
                dist[b] = dist[a] + cost

    for a, b, cost in edges:
        if dist[a] != INF and dist[a] + cost < dist[b]:
            return -1

    return dist


V, E = map(int, sys.stdin.readline().split())

edges = []
for _ in range(E):
    edge = list(map(int, sys.stdin.readline().split()))
    edges.append(edge)

ans = bellman_ford(V, 1, edges)

if ans == -1:
    print(-1)
else:
    ans = [-1 if x == float("inf") else x for x in ans[2:]]
    for i in ans:
        print(i)
