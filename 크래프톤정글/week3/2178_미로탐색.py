# 4 6
# 101111
# 101010
# 101011
# 111011

from collections import deque
import sys


N, M = map(int, sys.stdin.readline().split())

maze_map = []
visited = [[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    row = list(map(int, sys.stdin.readline().strip()))
    maze_map.append(row)

dq = deque()
result_cnt = 1
dq.append((0, 0, result_cnt))
dt = [(0, -1), (0, 1), (1, 0), (-1, 0)]
visited[0][0] = True


while len(dq) > 0:
    r, c, cnt = dq.popleft()
    if r == N - 1 and c == M - 1:
        result_cnt = cnt
        break
    for dr, dc in dt:
        if 0 <= r + dr < N and 0 <= c + dc < M:
            if maze_map[r + dr][c + dc] == 1 and not visited[r + dr][c + dc]:
                visited[r + dr][c + dc] = True
                dq.append((r + dr, c + dc, cnt + 1))

print(cnt)
