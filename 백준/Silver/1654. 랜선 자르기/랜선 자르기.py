import sys


N, M = map(int, sys.stdin.readline().split())
Klines = [int(sys.stdin.readline()) for _ in range(N)]


def soultions(Klines, goal):
    left, right = 1, max(Klines) + 1

    while left < right:
        mid = (left + right) // 2
        temp_goal = 0

        for line in Klines:
            temp_goal += line // mid

        if temp_goal >= goal:
            left = mid + 1
        else:
            right = mid
    return left - 1


print(soultions(Klines, M))