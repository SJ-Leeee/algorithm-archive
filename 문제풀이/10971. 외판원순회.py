# from itertools import permutations
# import sys


# N = int(sys.stdin.readline())

# t_map = []
# for i in range(N):
#     line = list(map(int, sys.stdin.readline().split()))
#     t_map.append(line)


# def lotate(t_map, city_order):
#     t_sum = 0
#     # tmap[0][2] > tmap[2][1] > tmap[1][3]...
#     for i in range(len(city_order) - 1):
#         cost = t_map[city_order[i]][city_order[i + 1]]

#         if cost == 0:
#             return False

#         t_sum += cost

#     first = t_map[0][city_order[0]]
#     last = t_map[city_order[-1]][0]

#     if first == 0 or last == 0:
#         return False

#     t_sum = t_sum + first + last

#     return t_sum


# N = int(sys.stdin.readline())

# t_map = []
# for i in range(N):
#     line = list(map(int, sys.stdin.readline().split()))
#     t_map.append(line)

# cities = [i for i in range(1, N)]
# # 0번 하자

# min_cost = float("inf")
# for perm in permutations(cities, N - 1):
#     ret = lotate(t_map, perm)
#     if not ret:
#         continue

#     min_cost = min(min_cost, ret)

# print(min_cost)


"""
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
"""

# 백트래킹 가지치기 (순열보다 조금더 빠름)

import sys


def dfs_recurse(cur, visited, cost, depth):
    global min_cost  # N과 min_cost의 차이점

    if cost >= min_cost:
        return

    if depth == N:
        if data[cur][0] > 0:
            min_cost = min(min_cost, cost + data[cur][0])
        return

    for n_city in range(N):
        if not visited[n_city] and data[cur][n_city] > 0:
            visited[n_city] = True
            dfs_recurse(n_city, visited, cost + data[cur][n_city], depth + 1)
            visited[n_city] = False


N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False] * N
visited[0] = True
min_cost = float("inf")

dfs_recurse(0, visited, 0, 1)

print(min_cost)
