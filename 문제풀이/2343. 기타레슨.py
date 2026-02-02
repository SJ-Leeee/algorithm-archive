# 9 3
# 1 2 3 4 5 6 7 8 9

# 최대 블루레이의 시간 = 강의 다 더한것 +1
# 최소 블루레이의 시간 = 1

import sys


N, M = map(int, sys.stdin.readline().split())
lectures = list(map(int, sys.stdin.readline().split()))

left = max(lectures)  # 강의보단 커야함
right = sum(lectures) + 1

while left < right:
    mid = (left + right) // 2  # 블루레이디스크의 최대시간
    blueray = [0] * M  # 새로 정해지면 초기화 해야함
    cur_blueray = 0  # 사용중인 블루레이 디스크
    condition = True

    for lect in lectures:
        if blueray[cur_blueray] + lect <= mid:
            blueray[cur_blueray] += lect
        else:  # 근데 초과하면 다음것
            cur_blueray += 1
            if cur_blueray >= M:  # 디스크가 초과하면
                condition = False
                break
            blueray[cur_blueray] += lect

    if condition:  # 통과했으면 최대값을 줄여봐야함
        right = mid
    else:  # 통과못했으면 최대값을 늘려봐야함
        left = mid + 1

print(left)

"""
5 3
10 10 10 20 30
"""
