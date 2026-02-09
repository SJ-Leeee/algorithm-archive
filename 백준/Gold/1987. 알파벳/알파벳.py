import sys


def dfs(row, col, guidemap, depth, visited, direct):
    max_depth = depth  # 현재 깊이로 시작

    for dr, dc in direct:
        nr, nc = row + dr, col + dc
        if 0 <= nr < R and 0 <= nc < C:
            if guidemap[nr][nc] not in visited:
                visited.add(guidemap[nr][nc])
                ret = dfs(nr, nc, guidemap, depth + 1, visited, direct)
                max_depth = max(max_depth, ret)
                visited.remove(guidemap[nr][nc])

    return max_depth


R, C = map(int, sys.stdin.readline().split())
guidemap = []
for _ in range(R):
    a = list(sys.stdin.readline().strip())
    guidemap.append(a)

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = set()
visited.add(guidemap[0][0])

ans = dfs(0, 0, guidemap, 1, visited, direct)
print(ans)
