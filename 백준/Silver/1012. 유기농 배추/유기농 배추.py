import sys

sys.setrecursionlimit(10**5)


def dfs(r, c, visited):
    for dr, dc in direct:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            if not visited[nr][nc] and farm[nr][nc] == 1:
                visited[nr][nc] = True
                dfs(nr, nc, visited)


T = int(sys.stdin.readline())
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(T):
    C, R, M = map(int, sys.stdin.readline().split())
    farm = [[0] * C for _ in range(R)]
    visited = [[False] * C for _ in range(R)]

    ans = 0

    for _ in range(M):
        c, r = map(int, sys.stdin.readline().split())
        farm[r][c] = 1

    for i in range(R):
        for j in range(C):
            if not visited[i][j] and farm[i][j] == 1:
                visited[i][j] = True
                dfs(i, j, visited)
                ans += 1

    print(ans)
