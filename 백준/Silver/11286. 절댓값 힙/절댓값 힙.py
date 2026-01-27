import heapq
import sys

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    
    if num == 0:
        print(heapq.heappop(heap)[1] if heap else 0)
    else:
        heapq.heappush(heap, (abs(num), num))  # (절댓값, 원본값)