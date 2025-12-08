"""
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10


1 0 0 1 1 0 0 1
"""

import sys


N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
sangeun_data = list(map(int, sys.stdin.readline().split()))

data.sort()
result = []
for i in range(M):
    start = 0
    end = len(data)

    while start < end:  # 이분탐색
        mid = (start + end) // 2

        if sangeun_data[i] > data[mid]:
            start = mid + 1
        else:
            end = mid

    if start < N and sangeun_data[i] == data[start]:  # 만약 찾는데이터가 존재하면
        result.append(1)
    else:  # 찾는데이터가 없었다면
        result.append(0)

print(*result)
