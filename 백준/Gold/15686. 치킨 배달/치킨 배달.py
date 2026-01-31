from itertools import combinations
import sys


def calc_distance(house, chicken):
    ret = 0
    for h_r, h_c in house:
        distance_chicken = 10**6
        for c_r, c_c in chicken:  # 치킨집에서 도는거
            distance_chicken = min(distance_chicken, abs(h_r - c_r) + abs(h_c - c_c))
        ret += distance_chicken

    return ret


N, M = map(int, sys.stdin.readline().split())
c_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

house_list = []
chicken_list = []

for i in range(N):
    for j in range(N):
        if c_map[i][j] == 1:
            house_list.append((i, j))
        elif c_map[i][j] == 2:
            chicken_list.append((i, j))

min_cost = float("inf")
for comb in combinations(chicken_list, M):
    min_cost = min(min_cost, calc_distance(house_list, comb))

print(min_cost)
