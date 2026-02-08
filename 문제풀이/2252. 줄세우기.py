"""
3 2
1 3
2 3

1 2 3

위상정렬
indegree
"""

from collections import deque
import sys


def topology_sort(graph, indegree, n):
    dq = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            dq.append(i)

    result = []
    while dq:
        v = dq.popleft()
        result.append(v)
        for nv in graph[v]:
            indegree[nv] -= 1
            if indegree[nv] == 0:
                dq.append(nv)

    if len(result) != n:
        return False

    return result


V, E = map(int, sys.stdin.readline().split())
graph = {}
for i in range(1, V + 1):
    graph[i] = []

indegree = [0] * (V + 1)
for _ in range(E):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    indegree[v2] += 1

ans = topology_sort(graph, indegree, V)
print(*ans)
