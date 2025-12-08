# 아이디어
# start, end를 두고
# width를 줄여가며 재귀함수를 호출
# start, end는 width에 따라 간격이 생김
# 재귀함수의 리턴값은 해당 width 순회의 가장큰 값
# 재귀함수 내부는 이전재귀에서 받은 값과 현재 순회의 값들을 비교
import sys


def mid_area(arr, start, end):
    mid = (start + end) // 2

    left = mid - 1
    right = mid + 1

    height = arr[mid]  # 초기 높이
    width = 1  # 초기 넓이

    max_area = -1
    while left >= start and right <= end:
        # 좌측은 시작점보다는 같거나 커야한다 그리고 우측은 엔드지점보다 같거나 작아야한다
        # 이러면 한쪽이 끝나면 자연스럽게 루프가 끝난다
        width += 1

        if arr[left] >= arr[right]:  # 좌측이 더 크다면
            height = min(height, arr[left])  # 작은 키에 맞춰서
            max_area = max(max_area, width * height)  # 넓이 구하기

            left -= 1
        else:
            height = min(height, arr[right])
            max_area = max(max_area, width * height)

            right += 1

    while left >= start:  # 좌측이 아직 남아있다면
        width += 1

        height = min(height, arr[left])
        max_area = max(max_area, width * height)

        left -= 1

    while right <= end:  # 우측이 아직 남아있다면
        width += 1

        height = min(height, arr[right])
        max_area = max(max_area, width * height)

        right += 1

    return max_area


#
# while low >=


def get_area(arr, start, end):
    if start == end:
        return arr[start]

    mid = (start + end) // 2

    left = get_area(arr, start, mid)
    right = get_area(arr, mid + 1, end)

    mid = mid_area(arr, start, end)
    return max(mid, left, right)


while True:
    data = list(map(int, sys.stdin.readline().split()))
    if data[0] == 0:
        break
    else:
        arr = data[1:]
        a = get_area(arr, 0, len(arr) - 1)
        print(a)
