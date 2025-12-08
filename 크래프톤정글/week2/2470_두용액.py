"""
투 포인터 문제

1.

"""

import sys


def two_liquid(arr):
    left = 0
    right = len(arr) - 1

    answer_1 = -1
    answer_2 = -1

    answer_min_diff = float("inf")
    while left < right:
        temp = arr[left] + arr[right]
        if answer_min_diff > abs(temp):  # temp가 좋은것
            answer_1 = arr[left]
            answer_2 = arr[right]
            answer_min_diff = abs(temp)

        if temp == 0:
            break
        elif temp > 0:
            right -= 1
        else:
            left += 1
    print(answer_1, answer_2)


N = sys.stdin.readline()
data = list(map(int, sys.stdin.readline().split()))
data.sort()
two_liquid(data)
