from collections import deque
import sys


N, L = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = []
# 큐에넣을 인덱스를 구한다.
dq = deque()

for i in range(N):
    while dq and dq[0][1] <= i - L:
        dq.popleft()

    while dq and dq[-1][0] >= arr[i]:
        dq.pop()

    dq.append((arr[i], i))

    ans.append(dq[0][0])


print(*ans)