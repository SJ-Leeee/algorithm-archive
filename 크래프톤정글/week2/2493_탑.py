import sys


N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))


def tower(arr):
    stack = []
    result = []
    for i, item in enumerate(arr):
        while len(stack) > 0:
            if item <= stack[-1][1]:  # 스택의 번호가 나보다 크다면
                result.append(stack[-1][0] + 1)
                stack.append((i, item))
                break

            stack.pop()

        if len(stack) == 0:
            result.append(0)
            stack.append((i, item))
        pass

    print(*result)


tower(arr)
