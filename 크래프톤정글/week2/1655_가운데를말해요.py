# 가장작은 n개중 맨뒤에것 얘기하면됨

# import heapq
# import sys

# 홀수라면
# idx = len(heap) // 2
# 짝수라면
# idx = len(heap) // 2 - 1

# N = int(sys.stdin.readline())

# heap = []
# for _ in range(N):
#     num = int(sys.stdin.readline())
#     heapq.heappush(heap, num)
#     if len(heap) % 2 == 0:
#         idx = len(heap) // 2
#         a = heapq.nsmallest(idx, heap)
#         print(a[-1])
#     else:
#         idx = len(heap) // 2 + 1
#         a = heapq.nsmallest(idx, heap)
#         print(a[-1])

# O(N^2 logN) > nsmallest가 nlogn 이다.


import heapq
import sys


leftheap = []
rightheap = []


N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    if len(leftheap) == 0 or -leftheap[0] > num:
        heapq.heappush(leftheap, -num)
    else:
        heapq.heappush(rightheap, num)

    if len(leftheap) > len(rightheap) + 1:
        move_node = -heapq.heappop(leftheap)
        heapq.heappush(rightheap, move_node)
    elif len(rightheap) > len(leftheap):
        move_node = heapq.heappop(rightheap)
        heapq.heappush(leftheap, -move_node)

    print(-leftheap[0])