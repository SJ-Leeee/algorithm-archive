# 4 6
# a t c i s w

from itertools import combinations
import sys


N, M = map(int, sys.stdin.readline().split())
chars = list(map(str, sys.stdin.readline().split()))
moum = ["a", "e", "i", "o", "u"]

moum_list = []
jaum_list = []
answer = []
for c in chars:
    if c in moum:
        moum_list.append(c)
    else:
        jaum_list.append(c)

max_moum = min(N - 2, len(moum_list))
for i in range(1, max_moum + 1):
    # 만약 개수가 안된다면 넘어가자
    if len(moum_list) < i or len(jaum_list) < N - i:
        continue

    for m_comb in combinations(moum_list, i):
        for j_comb in combinations(jaum_list, N - i):
            answer.append("".join(sorted(m_comb + j_comb)))

answer.sort()
for a in answer:
    print(a)
