"""
total_max 와
current_max를 만들기
"""

import sys


def lds():
    N = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    data = [-x for x in data]

    de_list = []
    de_list.append(data[0])

    for i in range(1, len(data)):
        if data[i] > de_list[-1]:
            de_list.append(data[i])
        else:
            left = lower_bound(de_list, data[i])
            de_list[left] = data[i]

    print(len(de_list))
    # else:


def lower_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


lds()
