"""
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
"""

from collections import deque
import sys


R, C = map(int, sys.stdin.readline().split())
pictures = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

visited = [[False] * C for _ in range(R)]
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dq = deque()
pict_cnt = 0
pict_max = 0
for i in range(R):
    for j in range(C):
        if not visited[i][j] and pictures[i][j] == 1:
            dq.append((i, j))
            temp_cnt = 0
            while dq:
                row, col = dq.popleft()

                if visited[row][col]:
                    continue

                visited[row][col] = True
                temp_cnt += 1

                for dr, dc in direct:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        if not visited[nr][nc] and pictures[nr][nc] == 1:
                            dq.append((nr, nc))
            pict_cnt += 1
            pict_max = max(pict_max, temp_cnt)

print(pict_cnt)
print(pict_max)
