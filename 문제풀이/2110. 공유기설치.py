"""
5 3
1
2
8
4
9

공유기 사이의 거리를 내가 정의한다.
거리가 이 이상은 되야한다.
최소거리 1
최대거리 끝과 끝

mid 부터 해보고
만약 cnt 가 넘었다
공유기가 부족하면 간격을 줄인다
공유기가 딱맞거나 더 많이 설치 됐으면 간격을 넓힌다.

이때 거리가 답
"""

import sys


N, M = map(int, sys.stdin.readline().split())
wifi = [int(sys.stdin.readline()) for _ in range(N)]
wifi.sort()

left, right = 1, wifi[-1] - wifi[0] + 1  # 최소거리 최대거리 반열린구간

answer = -1

while left < right:
    mid = (left + right) // 2  # 최대간격

    location = wifi[0]  # 현재위치
    cnt = 1
    for i in range(1, len(wifi)):
        if mid <= wifi[i] - location:  # 다음것과 내위치의 차이
            location = wifi[i]
            cnt += 1

    if cnt >= M:  # 만약 공유기가 충분히 설치될수있다면 간격을 넓혀봐야함
        left = mid + 1
    else:
        right = mid

print(left - 1)
