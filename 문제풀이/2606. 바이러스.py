# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

import sys


def dfs(v):
    global cnt
    visited[v] = True
    cnt += 1
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv)


V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
graph = {}
for i in range(1, V + 1):
    graph[i] = []

for _ in range(E):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (V + 1)
cnt = 0

dfs(1)
print(cnt - 1)
