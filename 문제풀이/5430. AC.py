"""
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
"""

"""
R = 뒤집기
D = 버리기

숫자가 큼.

RD = 뒤에거 버리기
RR 은 그냥 무시
기본은 pop left
R 들어가면 pop
"""

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
