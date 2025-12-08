# 8
# 11100110
# 11010010
# 10011010
# 11101100
# 01000111
# 00110001
# 11011000
# 11000111

# import heapq
# import sys


# N = int(sys.stdin.readline())

# maze = []
# cost = [[1000 for _ in range(N)] for _ in range(N)]
# for _ in range(N):
#     m_row = list(map(int, sys.stdin.readline().strip()))
#     maze.append(m_row)

# pq = []
# heapq.heappush(pq, (0, 0, 0))  # 시작지점
# dt = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 코스트가 같거나 크면 갈이유가없다.

# while pq:
#     row, col, crushed = heapq.heappop(pq)
#     if crushed >= cost[row][col]:
#         continue

#     # 벽을 깼나?
#     for dr, dc in dt:
#         next_r = row + dr
#         next_c = col + dc
#         if not (0 <= next_r < N and 0 <= next_c < N):
#             continue
#         new_crushed = crushed
#         if maze[next_r][next_c] == 0:
#             new_crushed += 1

#         if cost[next_r][next_c] > crushed:
#             cost[next_r][next_c] = new_crushed
#             heapq.heappush(pq, (crushed, next_r, next_c))

# print(cost)


# 8
# 11100110
# 11010010
# 10011010
# 11101100
# 01000111
# 00110001
# 11011000
# 11000111

import heapq
import sys


N = int(sys.stdin.readline())

maze = []

for _ in range(N):
    m_row = list(map(int, sys.stdin.readline().strip()))
    maze.append(m_row)


def miro(graph, start, end, N):
    visited = set()
    min_cost = [[float("inf") for _ in range(N)] for _ in range(N)]
    pq = []
    heapq.heappush(pq, (0, start))  # (0, (0,0))

    while pq:
        acc_cost, (r, c) = heapq.heappop(pq)
        if (r, c) in visited:
            continue
        visited.add((r, c))

        if acc_cost > min_cost[r][c]:
            continue

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_r = r + dr
            next_c = c + dc
            if 0 <= next_r < N and 0 <= next_c < N:
                is_break = 1 if graph[next_r][next_c] == 0 else 0
                if min_cost[next_r][next_c] > acc_cost + is_break:
                    min_cost[next_r][next_c] = acc_cost + is_break
                    heapq.heappush(pq, (acc_cost + is_break, (next_r, next_c)))

    e_r, e_c = end
    return min_cost[e_r][e_c]


re = miro(maze, (0, 0), (N - 1, N - 1), N)
print(re)
