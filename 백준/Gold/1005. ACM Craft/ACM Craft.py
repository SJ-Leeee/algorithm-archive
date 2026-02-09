from collections import deque
import sys


def acm_craft(graph, indgree, n, cost, find_b):
    dq = deque()

    time = cost[:]

    for i in range(1, n + 1):
        if indgree[i] == 0:
            dq.append((cost[i], i))

    while dq:
        c, v = dq.popleft()  # 이러면 30, 2 이 나옴
        # if v == find_b:
        #     break

        for nv in graph[v]:
            indgree[nv] -= 1
            time[nv] = max(time[nv], c + cost[nv])
            if indgree[nv] == 0:
                dq.append((time[nv], nv))

    return time[find_b]


M = int(sys.stdin.readline())
for _ in range(M):
    V, E = map(int, sys.stdin.readline().split())
    # 그래프, 진입차수
    graph = {}
    indgree = [0] * (V + 1)
    for i in range(1, V + 1):
        graph[i] = []

    # 인덱스 = 정잠 -1 / 물어보기
    cost = [0] + list(map(int, sys.stdin.readline().split()))

    for _ in range(E):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1].append(v2)
        indgree[v2] += 1

    building = int(sys.stdin.readline())

    ans = acm_craft(graph, indgree, V, cost, building)
    print(ans)