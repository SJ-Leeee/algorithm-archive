import heapq
import sys

left_heap = []
right_heap = []

N = int(sys.stdin.readline())
for i in range(1, N + 1):
    num = int(sys.stdin.readline())
    if i % 2 != 0:  # 홀수일경우
        if right_heap and right_heap[0] < num:  # 이상한 상황
            heapq.heappush(left_heap, -heapq.heappop(right_heap))
            heapq.heappush(right_heap, num)
        else:
            heapq.heappush(left_heap, -num)
    else:  # 짝수일경우
        if left_heap and -left_heap[0] > num:  # 이상한 상황
            heapq.heappush(right_heap, -heapq.heappop(left_heap))
            heapq.heappush(left_heap, -num)
        else:
            heapq.heappush(right_heap, num)

    print(-left_heap[0])
