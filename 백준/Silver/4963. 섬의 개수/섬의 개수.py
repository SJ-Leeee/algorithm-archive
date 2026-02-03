import sys

sys.setrecursionlimit(10**5)
def dfs_recurse(island, row, col):
    # 0,0 ~ -1, -1 까지 돌면서 False 면 dfs 돌리기
    # 상하좌우대각선
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
    visited = [[False] * col for _ in range(row)]
    cnt = 0

    def dfs(cr, cc):
        visited[cr][cc] = True

        for dr, dc in direct:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < row and 0 <= nc < col:  # 지도내부
                if not visited[nr][nc] and island[nr][nc] == 1:  # 방문한적 없고 1이면
                    dfs(nr, nc)

    for i in range(row):
        for j in range(col):
            if not visited[i][j] and island[i][j] == 1:  # 방문한적 없고 1이면
                cnt += 1
                dfs(i, j)

    return cnt


while True:
    col, row = map(int, sys.stdin.readline().split())
    if col == 0 and row == 0:
        break
    island = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
    print(dfs_recurse(island, row, col))
