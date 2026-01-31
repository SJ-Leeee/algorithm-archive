# [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# 나보다 같거나 낮으면 갈필요없다
# 나보나 높으면 갱신후 계속간다
from collections import deque


def solution(maps):

    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    dq = deque([(0, 0)])

    row = len(maps)
    col = len(maps[0])

    INF = float("inf")
    map_cnt = [[INF] * col for _ in range(row)]
    map_cnt[0][0] = 1
    while dq:
        r, c = dq.popleft()
        for dr, dc in direct:
            nr = r + dr
            nc = c + dc
            if 0 > nr or row <= nr or 0 > nc or col <= nc:
                continue
            if maps[nr][nc] == 0:
                continue
            if map_cnt[nr][nc] <= map_cnt[r][c]:
                continue

            map_cnt[nr][nc] = map_cnt[r][c] + 1
            dq.append((nr, nc))
            # 만약 못가면 pass
            # 나보다 같거나 낮으면 pass
            # 벽이면 pass
            # 그게아니라면 갱신하고 큐에추가
    return -1 if map_cnt[-1][-1] == INF else map_cnt[-1][-1]


solution(
    [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1],
    ]
)
