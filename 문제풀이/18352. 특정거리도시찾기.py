"""
4 4 2 1 도시개수 간선정보 특정거리 출발도시
1 2
1 3
2 3
2 4
"""

from collections import deque
import sys


V, M, K, S = map(int, sys.stdin.readline().split())
graph = {}
for i in range(1, V + 1):
    graph[i] = []

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)

dq = deque()
dq.append((S, 0))  # 시작지점 거리
visited = [False] * (V + 1)
ans = []
while dq:
    v, distance = dq.popleft()
    if visited[v]:
        continue
    if distance == K:  # 거리
        ans.append(v)
    visited[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            dq.append((neighbor, distance + 1))

ans.sort()

if not ans:
    print(-1)
else:
    for i in ans:
        print(i)
