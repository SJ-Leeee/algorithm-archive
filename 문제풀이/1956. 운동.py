"""
3 4
1 2 1
3 2 1
1 3 5
2 3 2

갔다오는것이 중요
벨만포드는 시작점으로부터 음수가 있는지 사이클이 있는지 확인가능
플로이드는 모든 정점의 최소쌍을 구할수 있음
다만 i 에서 i 로 가는건 0 으로 두고시작함


"""

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
