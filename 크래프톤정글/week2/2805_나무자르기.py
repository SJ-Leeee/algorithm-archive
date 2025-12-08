import sys

# 만약 나무가 한개면
# start 10
# end 10
# mid 10


def binary_search_value(arr, low, top, goal_value):
    if low > top:  # 범위가 끝났을 때
        return low - 1  # 마지막으로 가능했던 높이 반환

    mid_value = (low + top) // 2
    # 잘 맞던가 2차이로 좁혀지네

    w_sum = 0
    for i in range(len(arr) - 1, -1, -1):  # 어차피 맨 끝부터 자르기때문에 변하지않ㅇ음
        if arr[i] <= mid_value:  # 자를 수 있는 나무만
            break
        w_sum += arr[i] - mid_value

    if w_sum >= goal_value:
        return binary_search_value(arr, mid_value + 1, top, goal_value)
    else:
        return binary_search_value(arr, low, mid_value - 1, goal_value)


N, goal_value = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()


a = binary_search_value(data, 0, data[-1], goal_value)
print(a)


# if len(arr) == 1:
#     return arr[0] - goal_value  # 나무가 한개인 경우에
# if start_value > end_value:
#     return False

# mid_value = (start_value + end_value) // 2  # 중간값

# w_sum = 0
# for i in range(len(arr) - 1, -1, -1):  # 어차피 맨 끝부터 자르기때문에 변하지않ㅇ음
#     if w_sum > goal_value:
#         break
#     if arr[i] > mid_value:  # 자를 수 있는 나무만
#         w_sum += arr[i] - mid_value

# if w_sum == goal_value:
#     return mid_value
# elif w_sum > goal_value:
#     return binary_search_value(arr, mid_value + 1, end_value, goal_value)
# else:
#     return binary_search_value(arr, start_value, mid_value - 1, goal_value)
