from collections import deque
import sys


N = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))

# 삭제해가면서 만약 len이 0이면 0을 추가하는 방식


def tower(arr):
    stack = []
    result = []

    for idx, item in enumerate(arr):
        # 스택이 존재하면 비교한후에 스택에 가장 높은것만 남겨둔다.
        while stack:
            if item <= stack[-1][1]:
                result.append(stack[-1][0] + 1)
                stack.append((idx, item))
                break

            stack.pop()

        if not stack:
            result.append(0)
            stack.append((idx, item))

    print(*result)


tower(towers)