from collections import deque
import sys


N, K = map(int, sys.stdin.readline().split())

dq = deque(range(1, N + 1))

result = []

while len(dq) > 1:
    for _ in range(K - 1):
        dq.append(dq.popleft())

    result.append(dq.popleft())

result.append(dq[0])

a = ", ".join(map(str, result))
print(f"<{a}>")
