"""
큐의길이는 M 만큼
min 을 리스트에 넣으면 O(n) * O(m)
"""

from collections import deque
import sys


N, L = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = []
# 큐에넣을 인덱스를 구한다.
dq = deque()

for i in range(N):
    # 인덱스 범위를 초과하는 것을 모두 삭제한다.
    while dq and dq[0][1] <= i - L:
        dq.popleft()

    # 나보다 큰값들을 전부삭제한다 (어차피 쓸모 없음)
    while dq and dq[-1][0] >= arr[i]:
        dq.pop()

    # 작은값 + 나까지 dq 에 배치
    dq.append((arr[i], i))

    # 첫번째는 항상작은값
    ans.append(dq[0][0])


print(*ans)
