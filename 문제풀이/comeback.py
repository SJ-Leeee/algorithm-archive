# import sys

# A, B, V = map(int, sys.stdin.readline().split())


# def solutions(day, night, goal):
#     if goal <= day:
#         return 1

#     work = goal - day
#     oneday = day - night

#     if work % oneday:
#         return (work // oneday) + 2
#     else:
#         return (work // oneday) + 1


# answer = solutions(A, B, V)
# print(answer)


# import sys
# from collections import deque

# N = int(sys.stdin.readline())

# apple_map = [[False] * N for _ in range(N)]

# A = int(sys.stdin.readline())
# # 사과 지도
# for _ in range(A):
#     row, col = map(int, sys.stdin.readline().split())
#     apple_map[row - 1][col - 1] = True


# D = int(sys.stdin.readline())
# dir_change_dq = deque()
# # 방향
# for _ in range(D):
#     sec, direct = sys.stdin.readline().split()
#     sec = int(sec)

#     dir_change_dq.append((sec, direct))


# main_map = [[False] * N for _ in range(N)]
# main_map[0][0] = True

# # 머리와 꼬리위치
# head = [0, 0]
# tail_dq = deque()
# tail_dq.append(tuple(head))

# # 현재시간과 가야되는 시간
# now_sec = 0
# goal_sec = 500000

# # 지금 뱀의 방향
# direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# direct_idx = 0

# while True:
#     if dir_change_dq:
#         goal_sec, direct_char = dir_change_dq.popleft()
#     else:
#         goal_sec = 50000
#         direct_char = None  # 추가
#     escape = False

#     cnt = goal_sec - now_sec
#     dx, dy = direct[direct_idx]
#     for _ in range(cnt):
#         head[0] += dx
#         head[1] += dy
#         print(f"머리의 위치 = ${head}")
#         now_sec += 1
#         # 벽에 닿음
#         if 0 > head[0] or head[0] >= N or 0 > head[1] or head[1] >= N:
#             escape = True
#             break

#         # 자기 몸에 닿음
#         if main_map[head[0]][head[1]] == True:
#             escape = True
#             break

#         # 살았으면 머리 다시 넣기
#         tail_dq.append(tuple(head))
#         main_map[head[0]][head[1]] = True
#         # 사과가 아니라면 꼬리탈출
#         if apple_map[head[0]][head[1]] == False:
#             re_x, re_y = tail_dq.popleft()
#             main_map[re_x][re_y] = False
#         else:
#             apple_map[head[0]][head[1]] = False
#         print(tail_dq)
#     if escape:
#         break

#     if direct_char == "D":
#         direct_idx += 1
#     elif direct_char == "L":
#         direct_idx -= 1

#     if direct_idx < 0:
#         direct_idx = 3
#     elif direct_idx > 3:
#         direct_idx = 0

# print(now_sec)


# ----

"""
4 5 1
1 2
1 3
1 4
2 4
3 4
"""


# from collections import deque
# import sys


# class Graph:
#     def __init__(self):
#         self.adjacency_list = {}

#     def add_vertex(self, vertex):  # 정점 추가
#         if vertex not in self.adjacency_list:
#             self.adjacency_list[vertex] = []
#             return True
#         return False

#     def add_edge(self, v1, v2):
#         if not (v1 in self.adjacency_list and v2 in self.adjacency_list):
#             return False
#         self.adjacency_list[v1].append(v2)
#         self.adjacency_list[v2].append(v1)

#         self.adjacency_list[v1].sort()
#         self.adjacency_list[v2].sort()
#         return True

#     def dfs_recursive(self, start):
#         if start not in self.adjacency_list:
#             return False

#         visit = set()
#         result = []

#         def dfs(vertex):
#             visit.add(vertex)
#             result.append(vertex)

#             for neighbor in self.adjacency_list[vertex]:
#                 if neighbor not in visit:
#                     dfs(neighbor)

#         dfs(start)
#         return result

#     def bfs(self, start):
#         if start not in self.adjacency_list:
#             return False

#         visit = set()
#         dq = deque()
#         result = []
#         dq.append(start)
#         visit.add(start)

#         while len(dq) > 0:
#             vertex = dq.popleft()
#             result.append(vertex)
#             for neighbor in self.adjacency_list[vertex]:
#                 if neighbor not in visit:
#                     visit.add(neighbor)
#                     dq.append(neighbor)
#         return result


# graph = Graph()

# """
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# """

# V, E, S = map(int, sys.stdin.readline().split())

# for i in range(1, V + 1):
#     graph.add_vertex(i)

# for _ in range(E):
#     v1, v2 = map(int, sys.stdin.readline().split())
#     graph.add_edge(v1, v2)

# print(*graph.dfs_recursive(S))
# print(*graph.bfs(S))


# 4 6
# 101111
# 101010
# 101011
# 111011

# import sys

# sys.setrecursionlimit(10**6)

# N, M = map(int, sys.stdin.readline().split())
# dfs_map = []
# for _ in range(N):
#     inp = sys.stdin.readline().strip()
#     dfs_map.append(list(map(int, inp)))


# INF = 10**6
# cnt_map = [[INF] * M for _ in range(N)]

# cnt_map[0][0] = 1
# direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# def dfs(loca, x, y, cnt):
#     for dx, dy in direct:
#         nx = x + dx
#         ny = y + dy
#         if 0 <= nx < N and 0 <= ny < M:
#             if dfs_map[nx][ny] and cnt_map[nx][ny] > cnt + 1:
#                 cnt_map[nx][ny] = cnt + 1
#                 dfs(loca, nx, ny, cnt + 1)


# dfs(dfs_map, 0, 0, 1)


# print(cnt_map[N - 1][M - 1])


# from collections import deque
# import sys

# N, M = map(int, sys.stdin.readline().split())
# bfs_map = []
# for _ in range(N):
#     inp = sys.stdin.readline().strip()
#     bfs_map.append(list(map(int, inp)))

# visited = [[False] * M for _ in range(N)]
# result = [[-1] * M for _ in range(N)]

# result[0][0] = 1
# direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# dq = deque()
# dq.append((0, 0))
# visited[0][0] = True

# while len(dq) > 0:
#     x, y = dq.popleft()
#     for dx, dy in direct:
#         nx = x + dx
#         ny = y + dy
#         if 0 <= nx < N and 0 <= ny < M:
#             if bfs_map[nx][ny] and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 result[nx][ny] = result[x][y] + 1
#                 dq.append((nx, ny))


# print(result[N - 1][M - 1])


# 4 7
# 6 13
# 4 8
# 3 6
# 5 12

# import sys


# E, V = map(int, sys.stdin.readline().split())

# items = []
# for _ in range(E):
#     kg, val = map(int, sys.stdin.readline().split())
#     items.append((kg, val))

# dp = [[0] * (V + 1) for _ in range(E + 1)]

# for i in range(1, E + 1):
#     k, v = items[i - 1]
#     for mk in range(V + 1):
#         if k > mk:
#             dp[i][mk] = dp[i - 1][mk]
#         else:
#             dp[i][mk] = max(dp[i - 1][mk - k] + v, dp[i - 1][mk])

# print(dp[-1][-1])

# 2차원 배열 i는 물건의 개수, k는 키로그람이다


# 6
# 10
# 20
# 15
# 25
# 10
# 20

# import sys


# N = int(sys.stdin.readline())
# s = []
# dp = [0 for _ in range(N)]
# for _ in range(N):
#     stair = int(sys.stdin.readline())
#     s.append(stair)


# def stairs_dp():
#     dp[0] = s[0]
#     dp[1] = s[0] + s[1]
#     dp[2] = s[2] + max(s[0], s[1])

#     for i in range(3, N):
#         dp[i] = max(s[i] + s[i - 1] + dp[i - 3], dp[i - 2] + s[i])


# if N < 3:
#     print(sum(s))
# else:
#     stairs_dp()

# print(dp)


# import sys


# def cut_woods(arr, cutline):
#     ans = 0
#     for i in arr:
#         if i > cutline:
#             ans += i - cutline
#     return ans


# N, M = map(int, sys.stdin.readline().split())
# woods = list(map(int, sys.stdin.readline().split()))


# left = 0
# right = max(woods)

# while left < right:
#     mid = (left + right) // 2

#     if cut_woods(woods, mid) >= M:
#         left = mid + 1
#     else:
#         right = mid

# print(left - 1)

# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14

# import sys


# N = int(sys.stdin.readline())

# aa = []
# for _ in range(N):
#     start, end = map(int, sys.stdin.readline().split())
#     aa.append((start, end))

# aa.sort(key=lambda x: (x[1], x[0]))
# endtime = 0
# cnt = 0
# for i in aa:
#     if endtime <= i[0]:
#         endtime = i[1]
#         cnt += 1

# print(cnt)

"""
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
"""


# import sys


# N, M = map(int, sys.stdin.readline().split())
# coins = []
# for _ in range(N):
#     coins.append(int(sys.stdin.readline()))

# ans = 0
# for i in range(N - 1, -1, -1):
#     ans += M // coins[i]
#     M %= coins[i]
# print(ans)


"""
5
-2 4 -99 -1 98

슬라이딩 윈도우. 투포인터
"""


import sys

N = int(sys.stdin.readline())
waters = list(map(int, sys.stdin.readline().split()))


best_couple = ()
best_diff = 10**3
waters.sort()
left = 0
right = N - 1

while left < right:
    diff = waters[right] + waters[left]

    if diff == 0:
        best_couple = (waters[left], waters[right])
        break

    if best_diff > abs(diff):
        best_diff = abs(diff)
        best_couple = (waters[left], waters[right])

    if diff > 0:
        right -= 1
    else:
        left += 1

print(*best_couple)
