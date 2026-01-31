from collections import deque
import sys

dq = deque([[0, 0]])  # 시작 위치 추가
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

apple = [[False for _ in range(N)] for _ in range(N)]
for _ in range(M):
    row, col = map(int, sys.stdin.readline().split())
    apple[row - 1][col - 1] = True

visited = [[False for _ in range(N)] for _ in range(N)]
visited[0][0] = True  # 시작 위치 방문 처리

L = int(sys.stdin.readline())

snake_len = 1
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오 아래 왼 위

cur_loca = [0, 0]
direct_idx = 0

count = 0
is_game_over = False

for _ in range(L):
    change_second, rotate = sys.stdin.readline().split()
    change_second = int(change_second)

    if is_game_over:
        break

    # change_second초까지 이동
    while count < change_second:
        count += 1  # 시간 먼저 증가

        new_row = cur_loca[0] + direct[direct_idx][0]
        new_col = cur_loca[1] + direct[direct_idx][1]

        # 벽 충돌 체크
        if new_col >= N or new_col < 0 or new_row >= N or new_row < 0:
            is_game_over = True
            break

        # 자신의 몸 충돌 체크
        if visited[new_row][new_col]:
            is_game_over = True
            break

        # 이동 처리
        dq.append([new_row, new_col])
        visited[new_row][new_col] = True
        cur_loca = [new_row, new_col]

        # 사과 먹기
        if apple[new_row][new_col]:
            apple[new_row][new_col] = False
            snake_len += 1

        # 꼬리 처리
        while len(dq) > snake_len:
            r, c = dq.popleft()
            visited[r][c] = False

    # 방향 전환
    if not is_game_over:
        if rotate == "D":  # 오른쪽 회전
            direct_idx = (direct_idx + 1) % 4
        else:  # 왼쪽 회전 (L)
            direct_idx = (direct_idx - 1) % 4

# 남은 이동 (방향 전환이 끝난 후)
if not is_game_over:
    while True:
        count += 1  # 시간 먼저 증가

        new_row = cur_loca[0] + direct[direct_idx][0]
        new_col = cur_loca[1] + direct[direct_idx][1]

        if new_col >= N or new_col < 0 or new_row >= N or new_row < 0:
            break
        if visited[new_row][new_col]:
            break

        dq.append([new_row, new_col])
        visited[new_row][new_col] = True
        cur_loca = [new_row, new_col]

        if apple[new_row][new_col]:
            apple[new_row][new_col] = False  # 사과 제거 추가!
            snake_len += 1

        while len(dq) > snake_len:
            r, c = dq.popleft()
            visited[r][c] = False

print(count)  # count + 1이 아니라 count (이미 증가시켰으므로)
