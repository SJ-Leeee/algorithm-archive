"""
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
"""

import sys

sys.setrecursionlimit(10**6)


def dfs_recurse(graph, n):
    color = [-1] * (n + 1)

    def dfs(v):
        for nv in graph[v]:
            if color[nv] == color[v]:
                return False
            if color[nv] == -1:
                color[nv] = abs(color[v] - 1)
                if not dfs(nv):
                    return False
        return True

    for v in range(1, n + 1):
        if color[v] == -1:
            color[v] = 0
            if not dfs(v):  # ✅ 반환값 체크
                return False

    return True


N = int(sys.stdin.readline())
for _ in range(N):  # 케이스
    V, E = map(int, sys.stdin.readline().split())  # 정점과 간선
    graph = {}
    color = [-1] * (V + 1)  # -1 방문x, 1,0

    for i in range(1, V + 1):
        graph[i] = []

    for _ in range(E):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    ret = dfs_recurse(graph, V)
    print("YES") if ret else print("NO")
