# 동물 기준으로 순회
# 사대의 위치가 포함되면 cnt +=1
# hi = mid, low = mid+1 // start = 0, end = len -1 로 잡았을때

import sys


gun_num, animal_num, L = map(int, sys.stdin.readline().split())

guns = list(map(int, sys.stdin.readline().split()))

animals = []
for _ in range(animal_num):
    x, y = map(int, sys.stdin.readline().split())
    animals.append((x, y))

guns.sort()

cnt = 0
for location in animals:
    x, y = location
    if y > L:
        continue
    min_range = x - (L - y)
    max_range = x + (L - y)
    hi = len(guns)
    lo = 0

    while lo < hi:
        mid = (lo + hi) // 2

        if guns[mid] >= min_range and guns[mid] <= max_range:
            # 포함 된다면
            cnt += 1
            break
        elif guns[mid] < min_range:
            lo = mid + 1
        elif guns[mid] > max_range:
            hi = mid


print(cnt)


"""
이분탐색 기준!!!!!!!!

while left < right:
    mid = (left + right) // 2
    if arr[mid] < myItem:
        left = mid + 1
    else:
        right = mid  # mid-1이 아님!

"""
"""
arr = [1, 3, 5, 7, 9]

# myItem = 5인 경우
# 결과: left = 2 (arr[2] = 5, 정확한 위치!)

# myItem = 4인 경우  
# 결과: left = 2 (arr[2] = 5, 4 이상인 첫 위치)

# myItem = 6인 경우
# 결과: left = 3 (arr[3] = 7, 6 이상인 첫 위치)

# myItem = 10인 경우
# 결과: left = 5 (배열 길이, 모든 값보다 큼)

"""
