"""
순열알고리즘 사용

2
5 6
0 0 1 0
"""

from collections import deque
import sys


N = int(sys.stdin.readline())
dq = deque()

data = list(map(int, sys.stdin.readline().split()))

dq.extend(data)


operator = list(map(int, sys.stdin.readline().split()))


def calc(num1, num2, idx):
    if idx == 0:
        return num1 + num2
    elif idx == 1:
        return num1 - num2
    elif idx == 2:
        return num1 * num2
    else:
        re = abs(num1) // num2
        if num1 > 0:
            return re
        else:
            return -re


r_min = float("inf")
r_max = float("-inf")


def brute_force(dq, operator, depth, N):
    global r_min, r_max
    if depth == N:
        r_max = max(r_max, dq[0])
        r_min = min(r_min, dq[0])
        return

    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            a = dq.popleft()
            b = dq.popleft()
            result = calc(a, b, i)
            dq.appendleft(result)
            brute_force(dq, operator, depth + 1, N)
            operator[i] += 1
            dq.popleft()  # result 제거
            dq.appendleft(b)  # 원래 순서로 복구
            dq.appendleft(a)


brute_force(dq, operator, 0, N - 1)

print(r_max)
print(r_min)
