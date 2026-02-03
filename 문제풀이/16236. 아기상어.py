# 첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.

# 둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고,
# 아래와 같은 의미를 가진다.

# 0: 빈 칸
# 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
# 9: 아기 상어의 위치

"""
상어의 위치에서 가장 가까운 물고기를 먹어치우는 로직
생선들은 dict에 넣어버리면되고,
가까운거리부터 찾으면되는데 그럼 bfs를 위쪽 왼쪽으로 이어 나가야한다.
방향은 위 왼 오른 아래 순으로 이어간다.
순차대로 찾아나가는데 만약 발견했으면 초기화

4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
"""

# from collections import deque
# import sys


# N = int(sys.stdin.readline())
# sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# dq = deque()
# direct = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # 위 왼 오른 아래
# level = 2
# eat_cnt = 0
# sec = 0


# is_find = False
# visited = [[False] * N for _ in range(N)]
# distance = [[-1] * N for _ in range(N)]
# cur_loca = [-1, -1]
# for i in range(N):  # 시작지점 찾기
#     if is_find:
#         break
#     for j in range(N):
#         if sea[i][j] == 9:
#             dq.append((i, j))
#             is_find = True
#             distance[i][j] = 0
#             cur_loca = [i, j]
#             break

# while dq:
#     row, col = dq.popleft()

#     if visited[row][col]:  # 왔던자리라면(이것도 근데 안할수도있지않나)
#         continue
#     visited[row][col] = True

#     for dr, dc in direct:
#         nr, nc = row + dr, col + dc
#         # 기본적으로 들어와야함
#         if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
#             if 0 < sea[nr][nc] < level:  # 먹을수있다면
#                 sea[nr][nc] = 9  # 물고기 삭제
#                 sec += distance[row][col] + 1  # 시간추가
#                 cr, cc = cur_loca
#                 sea[cr][cc] = 0
#                 cur_loca = [nr, nc]
#                 # visited 초기화
#                 visited = [[False] * N for _ in range(N)]
#                 distance = [[-1] * N for _ in range(N)]
#                 distance[nr][nc] = 0

#                 # 시작점 초기화
#                 dq.clear()
#                 dq.append((nr, nc))
#                 # 먹은생선 1추가
#                 eat_cnt += 1
#                 if eat_cnt == level:
#                     level = level + 1 if level < 7 else 7
#                     eat_cnt = 0
#                 for i in sea:
#                     print(i)
#                 print(f"{level}------------------{sec}")
#                 break
#             if sea[nr][nc] <= level:  # 먹을수없다면 지나가기만
#                 dq.append((nr, nc))
#                 distance[nr][nc] = distance[row][col] + 1

# # print(sec)
# """

# 6
# 5 4 3 2 3 4
# 4 3 2 3 4 5
# 3 2 9 5 6 6
# 2 1 2 3 4 5
# 3 2 1 6 5 4
# 6 6 6 6 6 6
# (3,1) -> (4,2) -> lp -> 3,2 -> 2,1 -> 1,2 -> lp -> 0,2
# 0,3
# """


from collections import deque
import sys

N = int(sys.stdin.readline())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

direct = [(-1, 0), (0, -1), (0, 1), (1, 0)]
level = 2
eat_cnt = 0
sec = 0

# 시작 위치 찾기
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark_r, shark_c = i, j
            sea[i][j] = 0
            break

while True:
    visited = [[False] * N for _ in range(N)]
    distance = [[-1] * N for _ in range(N)]
    dq = deque([(shark_r, shark_c)])
    visited[shark_r][shark_c] = True
    distance[shark_r][shark_c] = 0

    candidates = []
    min_dist = float("inf")

    while dq:
        row, col = dq.popleft()

        # 이미 찾은 최소 거리보다 멀면 더 탐색할 필요 없음
        if distance[row][col] >= min_dist:
            continue

        for dr, dc in direct:
            nr, nc = row + dr, col + dc

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if sea[nr][nc] <= level:
                    visited[nr][nc] = True
                    distance[nr][nc] = distance[row][col] + 1
                    dq.append((nr, nc))

                    if 0 < sea[nr][nc] < level:
                        candidates.append((distance[nr][nc], nr, nc))
                        min_dist = min(min_dist, distance[nr][nc])

    if not candidates:
        break

    candidates.sort()
    dist, nr, nc = candidates[0]

    sec += dist
    sea[nr][nc] = 0
    shark_r, shark_c = nr, nc
    eat_cnt += 1

    if eat_cnt == level:
        level += 1
        eat_cnt = 0

print(sec)
