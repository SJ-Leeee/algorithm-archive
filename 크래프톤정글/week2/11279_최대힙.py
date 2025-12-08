import heapq
import sys


heap = []

N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, -num)
    else:
        if len(heap) != 0:
            print(-heapq.heappop(heap))
        else:
            print(0)
