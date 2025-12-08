from collections import deque
import heapq
import sys


data = []
pq = []
dq = deque()
N = int(sys.stdin.readline())
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    data.append((start, end))

data.sort()
dq.extend(data)

max_room = 0
while dq:
    start, end = dq.popleft()
    if not pq:
        heapq.heappush(pq, end)
    else:
        if pq[0] <= start:
            heapq.heappop(pq)
        heapq.heappush(pq, end)
    max_room = max(max_room, len(pq))

print(max_room)
