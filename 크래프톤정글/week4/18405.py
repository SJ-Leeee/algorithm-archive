"""
처음에만 순서대로 하는 bfs
"""

from collections import deque
import heapq
import sys


N, V = map(int, sys.stdin.readline().split())
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

virus_map = []

for _ in range(N):
    virus = list(map(int, sys.stdin.readline().split()))
    virus_map.append(virus)

S, X, Y = map(int, sys.stdin.readline().split())


def virus():
    if S == 0:
        print(virus_map[X - 1][Y - 1])
        return

    clean_zone = 0
    start_temp = []
    for r in range(N):
        for c in range(N):
            if virus_map[r][c]:

                start_temp.append((virus_map[r][c], r, c))
            else:
                clean_zone += 1
    start_temp.sort()
    dq = deque()
    dq.extend(start_temp)

    temp = []

    for _ in range(S):
        if clean_zone == 0:
            break
        while dq:
            virus, r, c = dq.popleft()

            for dr, dc in direct:
                n_r = r + dr
                n_c = c + dc
                if 0 <= n_r < N and 0 <= n_c < N:
                    if not virus_map[n_r][n_c]:
                        virus_map[n_r][n_c] = virus
                        temp.append((virus, n_r, n_c))

                        clean_zone -= 1
        dq.extend(temp)
        temp = []

    print(virus_map[X - 1][Y - 1])


virus()
# def bb():
#     if S == 0:
#         print(virus[X - 1][Y - 1])
#         return

#     clean_zone = 0
#     pq = deque()
#     visited = set()
#     aa = []
#     for r in range(N):
#         for c in range(N):
#             if virus_map[r][c]:
#                 visited.add((r, c))
#                 aa.append((virus_map[r][c], r, c))
#             else:
#                 clean_zone += 1
#     aa.sort()
#     pq.extend(aa)
#     temp_pq = []
#     for _ in range(S):  # S번 실행
#         if clean_zone == 0:
#             return
#         while pq:
#             virus, row, col = pq.popleft()

#             for dr, dc in direct:
#                 n_r = row + dr
#                 n_c = col + dc
#                 if 0 <= n_r < N and 0 <= n_c < N and not virus_map[n_r][n_c]:
#                     virus_map[n_r][n_c] = virus
#                     clean_zone -= 1
#                     temp_pq.append((virus, n_r, n_c))

#         pq.extend(temp_pq)

#     print(virus_map[X - 1][Y - 1])


# bb()
