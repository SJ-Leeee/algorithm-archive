import heapq
import sys


N = int(sys.stdin.readline())

minus_heap = []
plus_heap = []

for _ in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        if not minus_heap and not plus_heap:
            print(0)
        elif not minus_heap:
            print(heapq.heappop(plus_heap))
        elif not plus_heap:
            print(-heapq.heappop(minus_heap))
        else:
            (
                print(-heapq.heappop(minus_heap))
                if minus_heap[0] <= plus_heap[0]
                else print(heapq.heappop(plus_heap))
            )
    else:
        heapq.heappush(plus_heap, num) if num > 0 else heapq.heappush(minus_heap, -num)
