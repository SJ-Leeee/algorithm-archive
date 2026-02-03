from collections import deque
import sys

N = int(sys.stdin.readline())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

direct = [(-1, 0), (0, -1), (0, 1), (1, 0)]
level = 2
eat_cnt = 0
sec = 0

# 시작 위치 찾기
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark_r, shark_c = i, j
            sea[i][j] = 0
            break

while True:
    visited = [[False] * N for _ in range(N)]
    distance = [[-1] * N for _ in range(N)]
    dq = deque([(shark_r, shark_c)])
    visited[shark_r][shark_c] = True
    distance[shark_r][shark_c] = 0
    
    candidates = []
    min_dist = float('inf')
    
    while dq:
        row, col = dq.popleft()
        
        # 이미 찾은 최소 거리보다 멀면 더 탐색할 필요 없음
        if distance[row][col] >= min_dist:
            continue
        
        for dr, dc in direct:
            nr, nc = row + dr, col + dc
            
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if sea[nr][nc] <= level:
                    visited[nr][nc] = True
                    distance[nr][nc] = distance[row][col] + 1
                    dq.append((nr, nc))
                    
                    if 0 < sea[nr][nc] < level:
                        candidates.append((distance[nr][nc], nr, nc))
                        min_dist = min(min_dist, distance[nr][nc])
    
    if not candidates:
        break
    
    candidates.sort()
    dist, nr, nc = candidates[0]
    
    sec += dist
    sea[nr][nc] = 0
    shark_r, shark_c = nr, nc
    eat_cnt += 1
    
    if eat_cnt == level:
        level += 1
        eat_cnt = 0

print(sec)