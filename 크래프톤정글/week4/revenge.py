# 3
# 2
# 1 2
# 1000
# 3
# 1 5 10
# 100
# 2
# 5 7
# 22

# import sys


# S = int(sys.stdin.readline())

# for _ in range(S):
#     C = int(sys.stdin.readline())
#     coins = list(map(int, sys.stdin.readline().split()))
#     num = int(sys.stdin.readline())

#     dp = [0] * (num + 1)
#     dp[0] = 1

#     for coin in coins:
#         for i in range(num + 1):
#             if i >= coin:
#                 dp[i] += dp[i - coin]

#     print(dp)


# 2
# 5 7
# 22
# 2
# 5 7
# 22

# import sys


# I, K = map(int, sys.stdin.readline().split())
# items = []
# for _ in range(I):
#     kg, val = map(int, sys.stdin.readline().split())
#     items.append((kg, val))

# dp = [[0 for _ in range(K + 1)] for _ in range(len(items) + 1)]


# for i in range(1, len(items) + 1):
#     kg, val = items[i - 1]
#     for k in range(K + 1):
#         if kg > k:
#             dp[i][k] = dp[i - 1][k]
#         else:
#             dp[i][k] = max(dp[i - 1][k - kg] + val, dp[i - 1][k])

# print(dp[-1][-1])

# import sys

# N = int(sys.stdin.readline())
# data = list(map(int, sys.stdin.readline().split()))

# lis = [data[0]]
# for i in range(1, len(data)):
#     if data[i] > lis[-1]:
#         lis.append(data[i])
#     else:
#         left = 0
#         right = len(lis)

#         while left < right:
#             mid = (left + right) // 2

#             if data[i] > lis[mid]:
#                 left = mid + 1
#             else:
#                 right = mid

#         lis[left] = data[i]


# print(len(lis))


# import sys


# data = sys.stdin.readline().strip()


# n_sum = 0
# last_char = 0
# flag = False
# for i in range(len(data)):
#     if data[i] == "+":
#         number = -int(data[last_char:i]) if flag else int(data[last_char:i])
#         n_sum += number
#         last_char = i + 1
#     elif data[i] == "-":
#         number = int(data[last_char:i])
#         if not flag:
#             n_sum += number
#             flag = True
#         else:
#             n_sum -= number
#         last_char = i + 1

# n_sum += -int(data[last_char:]) if flag else int(data[last_char:])

# print(n_sum)
# print(last_char_flag)

# print(s_num)


# import sys


# N = int(sys.stdin.readline())
# meeting_room = []
# for _ in range(N):
#     start, end = map(int, sys.stdin.readline().split())
#     meeting_room.append((start, end))


# meeting_room.sort(key=lambda x: (x[1], x[0]))


# recent_end = meeting_room[0][1]
# cnt = 1
# for i in range(1, N):
#     if meeting_room[i][0] >= recent_end:
#         cnt += 1
#         recent_end = meeting_room[i][1]

# print(cnt)


# 신입사원
# import sys


# N = int(sys.stdin.readline())

# for _ in range(N):
#     M = int(sys.stdin.readline())
#     newbi = []
#     for _ in range(M):
#         interview, resume = map(int, sys.stdin.readline().split())
#         newbi.append((interview, resume))

#     newbi.sort()
#     cut_line = newbi[0][1]
#     cnt = 1
#     for i in range(1, M):
#         if newbi[i][1] < cut_line:
#             cnt += 1
#             cut_line = newbi[i][1]
#     print(cnt)


# import sys

# goal, N = map(int, sys.stdin.readline().split())
# small_stone = set()
# for _ in range(N):
#     s = int(sys.stdin.readline())
#     small_stone.add(s)

# max_speed = int((2 * goal) ** 0.5) + 1
# INF = float("inf")
# dp = [[INF for _ in range(max_speed + 1)] for _ in range(goal + 1)]

# if 2 not in small_stone:
#     dp[2][1] = 1

# for pos in range(2, goal + 1):
#     if pos in small_stone:
#         continue

#     for speed in range(1, max_speed + 1):
#         if dp[pos][speed] == INF:
#             continue

#         for n_speed in (speed - 1, speed, speed + 1):
#             if n_speed <= 0:
#                 continue
#             if n_speed > max_speed:
#                 continue

#             n_pos = pos + n_speed

#             if n_pos in small_stone:
#                 continue
#             if n_pos > goal:
#                 continue

#             dp[n_pos][n_speed] = min(dp[n_pos][n_speed], dp[pos][speed] + 1)


# result = min(dp[goal]) if min(dp[goal]) != INF else -1
# print(result)


"""
행곱순..
"""
# 3
# 5 3
# 3 2
# 2 6

import sys


N = int(sys.stdin.readline())
matrix = []
for _ in range(N):
    R, C = map(int, sys.stdin.readline().split())
    matrix.append((R, C))
INF = float("inf")
matrix_dp = [[INF for _ in range(N)] for _ in range(N)]


def matrix_min_product(x, y):
    if x >= y:
        return 0
    if matrix_dp[x][y] != INF:
        return matrix_dp[x][y]

    for k in range(x, y):
        matrix_dp[x][y] = min(
            matrix_dp[x][y],
            matrix_min_product(x, k)
            + matrix_min_product(k + 1, y)
            + matrix[x][0] * matrix[k][1] * matrix[y][1],
        )
    return matrix_dp[x][y]


a = matrix_min_product(0, N - 1)
print(a)
