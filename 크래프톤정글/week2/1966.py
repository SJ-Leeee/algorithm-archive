"""
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

"""

from collections import deque
import heapq
import sys

N = int(sys.stdin.readline())

for _ in range(N):
    data_num, find_idx = map(int, sys.stdin.readline().split())
    priority_data = list(map(int, sys.stdin.readline().split()))

    origin_data = deque()  # 우선순위와 인덱스를 넣을 데이터 큐
    heap_data = []  # 가장 큰 우선순위를 찾아줄 힙

    for idx, item in enumerate(priority_data):
        item = -item  # 최대힙 구현을 위해 음수화
        heap_data.append(item)  # 힙데이터에는 우선순위만
        origin_data.append([idx, item])  # 원본 데이터에는 인덱스까지 삽입

    heapq.heapify(heap_data)  # 데이터를 다 넣고 최대힙

    count = 1

    while len(origin_data) > 0:

        data = origin_data.popleft()  # 맨 앞 데이터를 제거
        if heap_data[0] == data[1]:  # 만약 우선순위가 가장 크다면
            if find_idx == data[0]:  # 찾는 인덱스와도 같다면
                break
            heapq.heappop(heap_data)  # 찾는 인덱스가 아니라면
            count += 1  # 순서증가
        else:  # 우선 순위가 아니라면
            origin_data.append(data)  # 다시 뒤로

    print(count)


# print(count)
