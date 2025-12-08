"""

  s       m       e
 [1,  2,  4,  8,  9]

1. |s - m| vs |m - e| 중 큰것에 설치 두개

"""

import sys


def setup_router(arr, router):
    gap_start = 1
    gap_end = arr[-1] - arr[0]

    while gap_start <= gap_end:
        mid = (gap_start + gap_end) // 2
        # 들어오면 카운트 초기화

        v_count = 1

        cur_idx = 0
        for i in range(1, len(arr)):  # 배열을 순회하며 갭이 넘는 곳에 공유기설치
            if mid <= arr[i] - arr[cur_idx]:
                v_count += 1
                cur_idx = i

        if v_count >= router:
            gap_start = mid + 1
        else:
            gap_end = mid - 1

    max_distance = gap_start - 1
    return max_distance


N, router = map(int, sys.stdin.readline().split())

data = [int(sys.stdin.readline()) for _ in range(N)]
data.sort()
a = setup_router(data, router)

print(a)
