from collections import deque
import sys


F, S, G, U, D = map(int, sys.stdin.readline().split())
INF = float("inf")
visited = [INF] * (F + 1)

dq = deque([(S, 0)])  # 시작점 출발


while dq:
    floor, cost = dq.popleft()

    if visited[floor] != INF:
        continue
    visited[floor] = cost

    up_floor = floor + U
    down_floor = floor - D

    if up_floor <= F:  # 최고층 보단 작아야함
        if cost + 1 < visited[up_floor]:
            dq.append((up_floor, cost + 1))

    if down_floor > 0:  # 0층 보단 커야함
        if cost + 1 < visited[down_floor]:
            dq.append((down_floor, cost + 1))

ans = visited[G] if visited[G] != INF else "use the stairs"
print(ans)