from collections import deque

def solution(maps):
    dq = deque()
    map_r = len(maps)
    map_c = len(maps[0])
    visited = [[-1] * map_c for _ in range(map_r)]

    dq.append((0, 0, 1))
    visited[0][0] = 0

    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    while dq:
        row, col, cost = dq.popleft()

        for dr, dc in direct:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < map_r and 0 <= nc < map_c:
                if maps[nr][nc] != 0 and visited[nr][nc] == -1:
                    visited[nr][nc] = cost + 1
                    dq.append((nr, nc, cost + 1))

    return visited[-1][-1]