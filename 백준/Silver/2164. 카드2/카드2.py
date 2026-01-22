from collections import deque
import sys

N = int(sys.stdin.readline())
dq = deque([i for i in range(1, N + 1)])

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())


print(dq[0])
