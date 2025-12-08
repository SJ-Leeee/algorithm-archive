import sys


def binary_search(arr, start, end, n):
    if start > end:
        return False

    mid = (start + end) // 2  # start 0, end 11, mid 5

    if n == arr[mid]:
        return True
    elif n > arr[mid]:
        return binary_search(arr, mid + 1, end, n)
    else:
        return binary_search(arr, start, mid - 1, n)


# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
M = int(sys.stdin.readline())
data2 = list(map(int, sys.stdin.readline().split()))

for i in data2:
    result = 1 if binary_search(data, 0, len(data) - 1, i) else 0
    print(result)
