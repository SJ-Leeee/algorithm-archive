import sys


def cut_woods(arr, cutline):
    ans = 0
    for i in arr:
        if i > cutline:
            ans += i - cutline
    return ans


N, M = map(int, sys.stdin.readline().split())
woods = list(map(int, sys.stdin.readline().split()))


left = 0
right = max(woods)

while left < right:
    mid = (left + right) // 2

    if cut_woods(woods, mid) >= M:
        left = mid + 1
    else:
        right = mid

print(left - 1)