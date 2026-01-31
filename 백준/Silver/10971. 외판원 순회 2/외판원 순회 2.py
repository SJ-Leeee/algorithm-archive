from itertools import permutations
import sys


# N = int(sys.stdin.readline())

# t_map = []
# for i in range(N):
#     line = list(map(int, sys.stdin.readline().split()))
#     t_map.append(line)


def lotate(t_map, city_order):
    t_sum = 0
    # tmap[0][2] > tmap[2][1] > tmap[1][3]...
    for i in range(len(city_order) - 1):
        cost = t_map[city_order[i]][city_order[i + 1]]

        if cost == 0:
            return False

        t_sum += cost

    first = t_map[0][city_order[0]]
    last = t_map[city_order[-1]][0]

    if first == 0 or last == 0:
        return False

    t_sum = t_sum + first + last

    return t_sum


N = int(sys.stdin.readline())

t_map = []
for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    t_map.append(line)

cities = [i for i in range(1, N)]
# 0번 하자

min_cost = float("inf")
for perm in permutations(cities, N - 1):
    ret = lotate(t_map, perm)
    if not ret:
        continue

    min_cost = min(min_cost, ret)

print(min_cost)
