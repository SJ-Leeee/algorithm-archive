# 2 7
# 2 3 2 3 1 2 7

import heapq
import sys

# max_outlet, electric = map(int, sys.stdin.readline().split())
# used_list = list(map(int, sys.stdin.readline().split()))

# pq = []

# using_cnt = [0] * (electric + 1)
# in_used = [False] * (electric + 1)

# for i in used_list:
#     using_cnt[i] += 1

# used_outlet = 0
# result = 0
# for i in used_list:
#     if in_used[i]:  # 이미 사용중이라면
#         using_cnt[i] -= 1  # 사용횟수 1회 차감
#         continue
#     # 사용중이 아닐때
#     if used_outlet < max_outlet:
#         in_used[i] = True  # 사용처리
#         using_cnt[i] -= 1  # 사용횟수 1회차감
#         heapq.heappush(pq, (using_cnt[i], i))  # pq 삽입
#         used_outlet += 1
#     else:
#         _, sub_i = heapq.heappop(pq)  # 빠진 콘센트
#         in_used[sub_i] = False  # 뺀 콘센트 처리
#         result += 1  # 콘센트 빠짐

#         in_used[i] = True
#         using_cnt[i] -= 1
#         heapq.heappush(pq, (using_cnt[i], i))

# print(result)


import heapq
import sys

max_outlet, electric = map(int, sys.stdin.readline().split())
used_list = list(map(int, sys.stdin.readline().split()))


using_cnt = [0] * (electric + 1)

for i in used_list:
    using_cnt[i] += 1

reverse_used_list = used_list[::-1]

in_used = [False] * (electric + 1)  # 사용중이누?

used_outlet = 0  # 몇개 사용중이누?
result = 0  # 몇번 뽑았누?
for i in used_list:
    if in_used[i]:  # 이미 사용중이라면
        continue
    # 사용중이 아닐때
    if used_outlet < max_outlet:
        in_used[i] = True  # 사용처리
        used_outlet += 1
    else:
        for u_i in reverse_used_list:
            if in_used[u_i]:
                in_used[u_i] = False
                result += 1
                break
        in_used[i] = True  # 사용처리

print(result)
