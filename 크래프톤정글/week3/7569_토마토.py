from collections import deque
import heapq
import sys


COL, ROW, FLOOR = map(int, sys.stdin.readline().split())

tomato_tower = []
days = [[[float("inf") for _ in range(COL)] for _ in range(ROW)] for _ in range(FLOOR)]
for _ in range(FLOOR):
    tomato_map = []
    for _ in range(ROW):
        tomato_line = list(map(int, sys.stdin.readline().split()))
        tomato_map.append(tomato_line)
    tomato_tower.append(tomato_map)


def ttttt(tower, days_map):
    visited = set()
    pq = deque()

    for i in range(FLOOR):
        for j in range(ROW):
            for k in range(COL):
                if tower[i][j][k] == 1:
                    pq.append((0, (i, j, k)))  # start지점 삽입
                    days_map[i][j][k] = 0

    while pq:  # 토마토 주위를 맴돌기
        day, cur_loca = pq.popleft()  # 가까운 일차의 날짜와 위치를 가져옴

        if cur_loca in visited:  # 이미 들렸다면 다음
            continue
        visited.add(cur_loca)  # 안들렸다면 방문처리

        f, r, c = cur_loca

        if (
            days_map[f][r][c] < day
        ):  # 현재날짜가 저장되어있는 최소값보다 크다면 의미없음
            continue

        if f - 1 >= 0:  # 아래층 전파
            if not tower[f - 1][r][c]:  # 아래층이 0이라면
                days_map[f - 1][r][c] = day + 1
                tower[f - 1][r][c] = 1
                pq.append((day + 1, (f - 1, r, c)))
            # elif tower[f - 1][r][c] == 1:  # 아래층이 1이라면
            #     if days_map[f - 1][r][c] > day:
            #         days_map[f - 1][r][c] = day
            #         pq.appendleft((day, (f - 1, r, c)))
        if f + 1 < FLOOR:  #
            if not tower[f + 1][r][c]:
                days_map[f + 1][r][c] = day + 1
                tower[f + 1][r][c] = 1
                pq.append((day + 1, (f + 1, r, c)))
            # elif tower[f + 1][r][c] == 1:
            #     if days_map[f + 1][r][c] > day:
            #         days_map[f + 1][r][c] = day
            #         pq.appendleft((day, (f + 1, r, c)))

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 상하좌우
            next_r = r + dr
            next_c = c + dc
            if 0 <= next_r < ROW and 0 <= next_c < COL:  # 일단 범위안에 있어야 하고
                if not tower[f][next_r][next_c]:  # 0 이라면
                    days_map[f][next_r][next_c] = day + 1
                    tower[f][next_r][next_c] = 1
                    pq.append((day + 1, (f, next_r, next_c)))
                # elif tower[f][next_r][next_c] == 1:
                #     if days_map[f][next_r][next_c] > day:
                #         days_map[f][next_r][next_c] = day
                #         pq.appendleft((day, (f, next_r, next_c)))  # 앞에 삽입

    max_day = -1
    for i in range(FLOOR):
        for j in range(ROW):
            for k in range(COL):
                if days_map[i][j][k] == float("inf"):
                    if tower[i][j][k] == 0:
                        return -1
                else:
                    max_day = max(max_day, days_map[i][j][k])
    return max_day


res_tomato = ttttt(tomato_tower, days)

print(res_tomato)
