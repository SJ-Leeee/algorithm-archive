# import heapq
# import sys

# N = int(sys.stdin.readline())

# data = []
# for i in range(N):
#     start, end = map(int, sys.stdin.readline().split())
#     data.append((start, end, i))
# data.sort()

# pq = []

# max_room_cnt = 0
# for start, end, idx in data:
#     if not pq:  # 없으면 그냥 삽입
#         heapq.heappush(pq, (end, start, idx))
#     elif start >= pq[0][0]:  # 있는데 없앨 수 있으면 없앰
#         heapq.heappop(pq)
#         heapq.heappush(pq, (end, start, idx))
#     else:  # 있는데 못없앰
#         heapq.heappush(pq, (end, start, idx))
# # 인덱스를 만들어서 이전값을 저장해두자


# print(max_room_cnt)


import sys

N = int(sys.stdin.readline())

data = []
for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    data.append((start, end))

data.sort(key=lambda x: (x[1], x[0]))  # 끝나는시간 먼저, 같으면 시작시간이 먼저
end_point = -1
result = 0
for start, end in data:
    if start >= end_point:
        result += 1
        end_point = end

print(result)
