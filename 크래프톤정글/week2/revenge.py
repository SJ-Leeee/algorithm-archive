# import sys

### 1920 수찾기

"""
5
4 1 5 2 3
5
1 3 7 9 5


1
1
0
0
1

4번째 라인 수들이 2번째라인 수들에 존재하는지 확인
"""

# N = int(sys.stdin.readline())
# standard_list = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())

# standard_list.sort()
# arr = list(map(int, sys.stdin.readline().split()))

# for i in range(M):
#     right = len(standard_list)
#     left = 0

#     while left < right:
#         mid = (right + left) // 2

#         if standard_list[mid] < arr[i]:
#             left = mid + 1
#         else:
#             right = mid

#     if left < M and standard_list[left] == arr[i]:
#         print(1)
#     else:
#         print(0)


### 2805 나무자르기
"""
상근이는 나무 M미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다. 
정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.

목재절단기는 다음과 같이 동작한다. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 
높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 
따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다. 예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 
상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 
상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.

상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다. 
이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.


4 7
20 15 10 17

15

1. 나무를 정렬
2. 0~최대나무의 길이
3. 내가 가능한 최대길이의 나무
    예시: 15m를 잘랐을 때 충분하면 15m 
"""


# def sum_woods(woods, cut):
#     result = 0
#     for wood in woods:
#         if wood > cut:
#             result += wood - cut
#     return result


# N, need = map(int, sys.stdin.readline().split())
# wood_list = list(map(int, sys.stdin.readline().split()))

# wood_list.sort()
# left = 0
# right = wood_list[-1]
# while left < right:
#     mid = (left + right) // 2
#     target = sum_woods(wood_list, mid)

#     if need < target:
#         left = mid + 1
#     else:
#         right = mid
# if sum_woods(wood_list, left) < need:
#     left = left - 1
# print(left)


"""
2110 공유기설치

첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 
둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

거리를 줄여보자
"""

# import sys


# def set_router(house_list, term):
#     count = 1
#     previous = house_list[0]
#     for i in range(1, len(house_list)):
#         if house_list[i] >= previous + term:
#             previous = house_list[i]
#             count += 1
#     return count


# N, router_n = map(int, sys.stdin.readline().split())
# house_list = []
# for _ in range(N):
#     house_list.append(int(sys.stdin.readline()))

# house_list.sort()

# left = 1
# right = house_list[-1] + 1

# while left < right:
#     mid = (left + right) // 2
#     set_count = set_router(house_list, mid)
#     if set_count >= router_n:
#         left = mid + 1
#     else:
#         right = mid

# print(left - 1)


"""
나랑 똑같은거는 패스하고
절대값을 기준으로 한번해보자
min_abs
"""
# import sys


# N = int(sys.stdin.readline())
# liquid_list = list(map(int, sys.stdin.readline().split()))

# liquid_list.sort()


# left = 0
# right = N - 1

# min_diff = float("inf")
# answer_1 = 0
# answer_2 = 0
# while left < right:
#     temp = liquid_list[left] + liquid_list[right]
#     if min_diff > abs(temp):
#         answer_1 = liquid_list[left]
#         answer_2 = liquid_list[right]
#         min_diff = abs(temp)

#     if temp > 0:
#         right -= 1
#     else:
#         left += 1

# print(answer_1, answer_2)


### 2630 색종이 만들기
"""
4분면을 잘 나눈것이 핵심
"""
# import sys


# N = int(sys.stdin.readline())

# squre = []
# blue_print = 0
# white_print = 0
# for _ in range(N):
#     row = list(map(int, sys.stdin.readline().split()))
#     squre.append(row)


# white_print = 0
# blue_print = 0


# def show_color_squre(squre, N):
#     global white_print, blue_print
#     list_sum = 0
#     for i in range(len(squre)):
#         list_sum += sum(squre[i])

#     if list_sum == N * N:
#         blue_print += 1
#         return
#     elif list_sum == 0:
#         white_print += 1
#         return
#     else:
#         half = N // 2

#         q1 = [row[half:] for row in squre[:half]]
#         q2 = [row[:half] for row in squre[:half]]
#         q3 = [row[:half] for row in squre[half:]]
#         q4 = [row[half:] for row in squre[half:]]
#         show_color_squre(q1, half)
#         show_color_squre(q2, half)
#         show_color_squre(q3, half)
#         show_color_squre(q4, half)
#         return


# show_color_squre(squre, N)
# print(white_print)
# print(blue_print)


### 1629 곱셈

# import sys


# # N, power, mod = map(int, sys.stdin.readline().split())


# def powerpower(N, power, mod):
#     if power == 1:
#         return N % mod

#     if power % 2 == 0:
#         a = powerpower(N, power // 2, mod)
#         return (a * a) % mod
#     else:
#         half = power // 2
#         a = powerpower(N, half, mod)
#         b = powerpower(N, power - half, mod)
#         return (a * b) % mod


# # a = powerpower(N, power, mod)
# # print(a)

# a = [1, 2, 3]
# print(*a)

### 3190 뱀

"""
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

"""
from collections import deque
import sys

dq = deque()
direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
direct_n = 0
N = int(sys.stdin.readline())
apple_N = int(sys.stdin.readline())

visited = [[False for _ in range(N)] for _ in range(N)]
apple = [[False for _ in range(N)] for _ in range(N)]


for _ in range(apple_N):
    row, col = map(int, sys.stdin.readline().split())
    apple[row - 1][col - 1] = True


change_N = int(sys.stdin.readline())
snake_len = 1
prev_count = 0
cur_location = [0, 0]
dq.append(cur_location)

result_count = 0

game_over = False

for i in range(change_N):
    if game_over:
        break
    change_count, change_way = sys.stdin.readline().split()
    change_count = int(change_count)

    while result_count < change_count:
        result_count += 1

        new_row = cur_location[0] + direct[direct_n][0]
        new_col = cur_location[1] + direct[direct_n][1]
        cur_location = [new_row, new_col]

        if new_row >= N or new_col >= N or new_row < 0 or new_col < 0:
            game_over = True
            break  # 여기서 나간거 밖에서도 처리
        if visited[new_row][new_col] == True:
            game_over = True
            break  # 여기서 나간거 밖에서도 처리
        if apple[new_row][new_col] == True:
            apple[new_row][new_col] = False
            snake_len += 1

        dq.append(cur_location)
        visited[new_row][new_col] = True

        while len(dq) > snake_len:
            r, c = dq.popleft()
            visited[r][c] = False

    if change_way == "D":
        direct_n = direct_n + 1 if direct_n < 3 else 0
    else:
        direct_n = direct_n - 1 if direct_n > 0 else 3

while not game_over:
    result_count += 1

    new_row = cur_location[0] + direct[direct_n][0]
    new_col = cur_location[1] + direct[direct_n][1]
    cur_location = [new_row, new_col]

    if new_row >= N or new_col >= N or new_row < 0 or new_col < 0:
        game_over = True
        break  # 여기서 나간거 밖에서도 처리
    if visited[new_row][new_col] == True:
        game_over = True
        break  # 여기서 나간거 밖에서도 처리
    if apple[new_row][new_col] == True:
        snake_len += 1

    dq.append(cur_location)
    visited[new_row][new_col] = True

    while len(dq) < snake_len:
        r, c = dq.popleft()
        visited[r][c] = False

print(result_count)
