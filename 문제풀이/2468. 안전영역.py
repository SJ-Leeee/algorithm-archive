"""
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

높이는 최소부터 최대까지
"""

import sys

sys.setrecursionlimit(10**5)


def dfs_recurse(n):
    visited = [[False] * N for _ in range(N)]
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ret = 0

    def dfs(row, col):
        visited[row][col] = True

        for dr, dc in direct:
            nr, nc = row + dr, col + dc
            if 0 <= nr < N and 0 <= nc < N:  # 범위내
                if not visited[nr][nc] and region[nr][nc] > n:  # 안전구역?
                    dfs(nr, nc)

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and region[i][j] > n:
                dfs(i, j)
                ret += 1

    return ret


N = int(sys.stdin.readline())

region = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_rain = 0

for i in range(N):
    for j in range(N):
        max_rain = max(region[i][j], max_rain)

ans = [0] * (max_rain + 1)

for rain in range(0, max_rain):
    ans[rain] = dfs_recurse(rain)

print(max(ans))
