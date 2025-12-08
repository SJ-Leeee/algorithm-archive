# 3 2
# 1 3
# 2 3

from collections import deque
import sys


def dfs(graph, indgree):
    result = []
    visited = set()
    dq = deque()
    for i in range(1, len(indgree)):
        if not indgree[i]:
            dq.append(i)

    while dq:
        ver = dq.popleft()

        if ver in visited:
            continue

        result.append(ver)
        visited.add(ver)

        for i in graph[ver]:
            indgree[i] -= 1
            if not indgree[i]:
                dq.append(i)

    print(*result)


V, E = map(int, sys.stdin.readline().split())

indgree = [0] * (V + 1)

graph = {}
for i in range(1, V + 1):
    graph[i] = []

for _ in range(E):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    indgree[v2] += 1

dfs(graph, indgree)
