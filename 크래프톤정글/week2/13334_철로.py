# 둘중 작은것이 무조건 i[0]
# i[1]을 기준으로 잡고 라인 스위핑
# 현재위치 - 철로 <= i[0] <= 현재위치 라면 힙에 삽입
# 큐의 첫번째 것이 철로를 벗어났으면 pop
# 큐 순회 시 항상 max값 최신화

import heapq
from operator import itemgetter
import sys


N = int(sys.stdin.readline())
data = []
heap = []
for _ in range(N):
    x1, x2 = map(int, sys.stdin.readline().split())
    if x2 > x1:
        data.append([x1, x2])
    else:
        data.append([x2, x1])

railway = int(sys.stdin.readline())

data.sort(key=itemgetter(1, 0))
max_people = -1
for item in data:  # 순회
    cur_loca = item[1]  # 이 사람의 먼부분
    limit_zone = cur_loca - railway  # 한계지점 설정

    if item[0] >= limit_zone:  # 한계지점보다 크면
        heapq.heappush(heap, item)

    while (
        len(heap) > 0 and heap[0][0] < limit_zone
    ):  # heap안에 있는것들중 한계지점을 넘는것을 pop
        heapq.heappop(heap)

    max_people = max(max_people, len(heap))

print(max_people)
