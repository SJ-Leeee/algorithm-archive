"""
1. 0,0 부터 순회 P일때만
    1-1 origin 정해놓고 상하좌우 조지기 만약 X 라면 패스해도된다.
"""

from collections import deque


def check_map(place):
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    for x in range(5):
        for y in range(5):
            if place[x][y] != "P":  # P가 아니라면 다음것
                continue

            visited = [[False] * 5 for _ in range(5)]  # P라면 새로운 visited 생성
            visited[x][y] = True
            queue = deque([(x, y, 0)])

            while queue:
                cx, cy, dist = queue.popleft()

                for dx, dy in direct:
                    nx = cx + dx
                    ny = cy + dy

                    if not (0 <= nx < 5 and 0 <= ny < 5):  # 범위안에 들지못하면 다음것
                        continue

                    if visited[nx][ny]:  # 이미 방문했으면 다음것
                        continue

                    if place[nx][ny] == "P":  # P를 만났다면 0 반환 끝
                        return 0

                    if place[nx][ny] == "X":  # X 만났으면 더이상못감
                        continue

                    if dist + 1 < 2:
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))

    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(check_map(place))

    return answer


sample = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
]

solution(sample)
