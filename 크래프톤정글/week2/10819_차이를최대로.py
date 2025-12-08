import sys


diff_max = -1


def sum_diff_list(arr):
    temp = []
    for i in range(0, len(arr) - 1):
        diff_abs = abs(arr[i] - arr[i + 1])
        temp.append(diff_abs)

    return sum(temp)


def permutation_visited(arr, result, visited, depth, r):
    global diff_max

    if depth == r:
        check_max = sum_diff_list(result)
        diff_max = diff_max if diff_max >= check_max else check_max
        return

    for i in range(len(arr)):  # 항상 모든원소를 순회
        if not visited[i]:  # 원소가 선택되지 않았더라면
            visited[i] = True  # 해당원소 사용
            result[depth] = arr[i]  # 현재깊이에 원소사용
            permutation_visited(arr, result, visited, depth + 1, r)  # 다음깊이 순회
            visited[i] = False  # 해당원소 사용중지


N = int(input())
data = list(map(int, input().split()))
result = [0] * len(data)
visited = [False] * len(data)
r = len(data)
permutation_visited(data, result, visited, 0, r)
print(diff_max)
# 6
# 20 1 15 8 4 10
