import sys
from collections import deque


T = int(sys.stdin.readline())
for _ in range(T):
    command = sys.stdin.readline()
    length = int(sys.stdin.readline())
    t = sys.stdin.readline().strip().strip("[]")
    dq = deque(map(int, t.split(","))) if t else deque()

    isLeft = True
    isError = False
    for i in command:
        if i == "R":
            isLeft = False if isLeft else True

        if i == "D":
            if not dq:
                isError = True
                break
            dq.popleft() if isLeft else dq.pop()

    # dq.reverse() if not isLeft else None

    if not isLeft:
        dq.reverse()

    print(str(list(dq)).replace(" ", "")) if not isError else print("error")
