"""
5
1 3 2 -1 # v v1 c1 ... -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
"""

import sys

sys.setrecursionlimit(10**5)


def find_farthest(start, graph):
    visited = [False] * (len(graph) + 1)
    result = (start, 0)

    def dfs(v, cost):
        nonlocal result
        visited[v] = True

        if cost > result[1]:
            result = (v, cost)

        for nv, nc in graph[v]:
            if not visited[nv]:
                dfs(nv, cost + nc)

    dfs(start, 0)
    return result


V = int(sys.stdin.readline())
graph = {}
for i in range(1, V + 1):
    graph[i] = []

for _ in range(1, V + 1):
    info = list(map(int, sys.stdin.readline().split()))
    v = info[0]  # 첫 번째 숫자가 노드 번호
    for i in range(1, len(info) - 1, 2):
        graph[v].append((info[i], info[i + 1]))


# 어쨌든 부모를 하나 찾아서 거기서 dfs한번돌리면 끝일듯


parent, cost = find_farthest(1, graph)


ans_p, ans_c = find_farthest(parent, graph)
print(ans_c)
