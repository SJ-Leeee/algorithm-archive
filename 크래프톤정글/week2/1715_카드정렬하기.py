"""
sum = 제일작은것 넣어두고 10

suffle = sum + 최소요소 10 + 20

sum = sum + suffle 10 + 20
next
suffle = 30 + 40
sum = sum + suffle 30 + 70
"""

import heapq
import sys

N = int(sys.stdin.readline())

data = []

for _ in range(N):
    item = int(sys.stdin.readline())
    heapq.heappush(data, item)

accumulation_sum = 0


while len(data) > 1:
    first = heapq.heappop(data)
    second = heapq.heappop(data)
    suffle = first + second
    accumulation_sum += suffle
    heapq.heappush(data, suffle)


if N == 1:
    print(0)
else:
    print(accumulation_sum)
