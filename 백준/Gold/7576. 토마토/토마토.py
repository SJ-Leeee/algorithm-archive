from collections import deque
import sys


C, R = map(int, sys.stdin.readline().split())
tomatos = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
INF = float("inf")
day_cnt = [[INF] * C for _ in range(R)]  # 익는날짜 저장
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]


dq = deque()


for i in range(R):  # 토마토가 1일때마다 dq에 삽입
    for j in range(C):
        if tomatos[i][j] == 1:
            day_cnt[i][j] = 0  # 시작지점
            dq.append((i, j, 0))  # row, col, cost


while dq:
    r, c, day = dq.popleft()

    if day > day_cnt[r][c]:  # 만약 더 큰값이라면
        continue

    for dr, dc in direct:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            if tomatos[nr][nc] == 0 and day_cnt[nr][nc] > day + 1:

                day_cnt[nr][nc] = day + 1
                dq.append((nr, nc, day + 1))


ans = -1
is_done = False
for i in range(R):
    if is_done:
        break
    for j in range(C):
        if day_cnt[i][j] == INF:  # 만약 도달하지 않았다면
            if tomatos[i][j] != -1:
                ans = -1
                is_done = True
                break
            continue
        ans = max(ans, day_cnt[i][j])  # 높은숫자 저장

print(ans)