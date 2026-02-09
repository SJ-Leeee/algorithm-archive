"""
1, 2, 3, 4 > 기본부품
7
8
5 1 2
5 2 2
7 5 2
6 5 2
6 3 3
6 4 4
7 6 3
7 4 5
[1, 2, 5, 3, 4, 6, 7]
그다음에 7부터 돌리면 될듯
nv in 7
4, 6인데
만약 4이하면 추가하고
아니면
5를 만들때 1 두개 2 두개 가 필요하다
이거 dfs로는 안되나
"""

from collections import deque
import sys


V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

revers_graph = {}
count = [[0] * (V + 1) for _ in range(V + 1)]
indgree = [0] * (V + 1)
for i in range(1, V + 1):
    revers_graph[i] = []


for _ in range(E):
    v1, v2, cost = map(int, sys.stdin.readline().split())
    revers_graph[v2].append((cost, v1))
    indgree[v1] += 1

dq = deque()
for i in range(1, V + 1):
    if indgree[i] == 0:
        count[i][i] = 1
        dq.append(i)

while dq:
    current = dq.popleft()

    for ncost, nv in revers_graph[current]:  # 5 . 2 6
        indgree[nv] -= 1
        for i in range(1, V + 1):
            count[nv][i] += count[current][i] * ncost  # 다음거만들재료

        if indgree[nv] == 0:
            dq.append(nv)

# [i][i] 가 1이면서 [V][i] 는

for i in range(1, V + 1):
    if count[i][i] == 1 and count[V][i] > 0:
        print(i, count[V][i])
