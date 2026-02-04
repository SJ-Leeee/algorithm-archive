
import sys


def dfs(row, col, visited):
    visited[row][col] = True
    cnt = 1
    for dr, dc in direct:
        nr, nc = row + dr, col + dc
        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc] and villages[nr][nc] == 1:
                cnt += dfs(nr, nc, visited)

    return cnt


N = int(sys.stdin.readline())
villages = [[int(x) for x in sys.stdin.readline().strip()] for _ in range(N)]
visited = [[False] * N for _ in range(N)]
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

ans = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and villages[i][j] == 1:
            ans.append(dfs(i, j, visited))

ans.sort()
print(len(ans))
for i in ans:
    print(i)
