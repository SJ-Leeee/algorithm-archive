# 2 2
# 3 5
# 2 9

import sys


N, M = map(int, sys.stdin.readline().split())
list1 = list(map(int, sys.stdin.readline().split()))
list2 = list(map(int, sys.stdin.readline().split()))

answer = []
i = 0
j = 0


while i < N and j < M:
    if list1[i] < list2[j]:
        answer.append(list1[i])
        i += 1
    else:
        answer.append(list2[j])
        j += 1

while i < N:
    answer.append(list1[i])
    i += 1

while j < M:
    answer.append(list2[j])
    j += 1
print(*answer)
