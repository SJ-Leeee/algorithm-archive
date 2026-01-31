from itertools import permutations
import sys


def lotate(t_map, city_order):
    t_sum = 0
    # tmap[0][2] > tmap[2][1] > tmap[1][3]...
    for i in range(len(t_map)):
        if i == len(t_map) - 1:
            cost = t_map[city_order[i]][city_order[0]]
        else:
            cost = t_map[city_order[i]][city_order[i + 1]]

        if cost == 0:
            return False

        t_sum += cost

    return t_sum


N = int(sys.stdin.readline())

t_map = []
for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    t_map.append(line)

cities = [i for i in range(N)]

min_cost = float('inf')
for perm in permutations(cities, N):
    ret = lotate(t_map, perm)
    if not ret:
        continue

    min_cost = min(min_cost, ret)

print(min_cost)
