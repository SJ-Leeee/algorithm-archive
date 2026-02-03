# 6 5 정점의개수 간선의개수
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6

from collections import deque
import sys


V, E = map(int, sys.stdin.readline().split())
graph = {}

for i in range(1, V + 1):
    graph[i] = []

for _ in range(E):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (V + 1)  # idx = 0~V

dq = deque()
count = 0
for i in range(1, V + 1):
    if not visited[i]:

        dq.append(i)  # 1을 삽입
        count += 1
    while dq:

        v = dq.popleft()

        for nv in graph[v]:
            if not visited[nv]:
                dq.append(nv)
                visited[nv] = True

print(count)

# dfs로 풀어보기
import sys

sys.setrecursionlimit(10000)

V, E = map(int, sys.stdin.readline().split())
graph = {}

for i in range(1, V + 1):
    graph[i] = []

for _ in range(E):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (V + 1)  # idx = 0~V


def dfs(v):
    visited[v] = True
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv)


count = 0
for i in range(1, V + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
