import sys

sys.setrecursionlimit(10**5)


def normal(row, col, visited):
    for dr, dc in direct:
        nr, nc = row + dr, col + dc

        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc] and pictures[row][col] == pictures[nr][nc]:
                visited[nr][nc] = True
                normal(nr, nc, visited)


def blind(row, col, visited):
    for dr, dc in direct:
        nr, nc = row + dr, col + dc

        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc]:
                is_pass = False
                c1 = pictures[row][col]
                c2 = pictures[nr][nc]
                if (c1 == c2) or (c1 in blind_color and c2 in blind_color):
                    is_pass = True

                if is_pass:
                    visited[nr][nc] = True
                    blind(nr, nc, visited)


blind_color = ["R", "G"]

N = int(sys.stdin.readline())
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

pictures = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited_n = [[False] * N for _ in range(N)]
visited_b = [[False] * N for _ in range(N)]

n = 0
b = 0

for i in range(N):
    for j in range(N):
        if not visited_n[i][j]:
            visited_n[i][j] = True
            normal(i, j, visited_n)
            n += 1

        if not visited_b[i][j]:
            visited_b[i][j] = True
            blind(i, j, visited_b)
            b += 1

print(n, b)