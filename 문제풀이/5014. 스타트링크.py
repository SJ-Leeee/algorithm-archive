# 10 1 10 2 1  / F, S, G, U, D
# 스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고, 스타트링크가 있는 곳의 위치는 G층이다.
# 강호가 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동하려고 한다.

# 10층 건물 1층에서 10층으로 가야하고
# 2층씩 올라가는 U
# 1층씩 덜어지는 D

# dp도 되고 bfs도 될듯.

from collections import deque
import sys


F, S, G, U, D = map(int, sys.stdin.readline().split())
INF = float("inf")
visited = [INF] * (F + 1)

dq = deque([(S, 0)])  # 시작점 출발


while dq:
    floor, cost = dq.popleft()

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


# 12 2 10 3 1
