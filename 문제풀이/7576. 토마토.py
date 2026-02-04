"""
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

bfs 다만 익는 날짜를 구해야함
1에 대해서 모두 bfs를 돌리는데
모든 1에 대해서 돌리면..시간초과날것같기도한대 방법이 없을듯.

전역적으로 익는날짜 배열 필요함
visited 배열 필요하고

만약 토마토가 -1이 아니고 익는날짜가 -1이면 안익은게 있는거니까 -1 리턴
모든배열을 돌았을때 가장 큰값을 출력하면됨.
"""

# from collections import deque
# import sys


# def bfs(row, col):
#     dq = deque([(row, col)])
#     visited = [[False] * C for _ in range(R)]
#     day_cnt[row][col] = 0  # 시작지점

#     while dq:
#         r, c = dq.popleft()

#         if visited[r][c]:
#             continue
#         visited[r][c] = True

#         for dr, dc in direct:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
#                 if tomatos[nr][nc] == 0:
#                     day_cnt[nr][nc] = min(day_cnt[nr][nc], day_cnt[r][c] + 1)
#                     dq.append((nr, nc))


# C, R = map(int, sys.stdin.readline().split())
# tomatos = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
# INF = float("inf")
# day_cnt = [[INF] * C for _ in range(R)]  # 익는날짜 저장
# direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# for i in range(R):  # 토마토가 1일때마다 bfs해야함
#     for j in range(C):
#         if tomatos[i][j] == 1:
#             bfs(i, j)

# ans = -1
# is_done = False
# for i in range(R):
#     if is_done:
#         break
#     for j in range(C):
#         if day_cnt[i][j] == INF:  # 만약 도달하지 않았다면
#             if tomatos[i][j] != -1:
#                 ans = -1
#                 is_done = True
#                 break
#             continue
#         ans = max(ans, day_cnt[i][j])  # 높은숫자 저장

# print(ans)


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
# for i in day_cnt:
# print(i)
