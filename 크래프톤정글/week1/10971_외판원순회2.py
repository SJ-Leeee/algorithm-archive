# """
# 일반적인 순열과 비슷함

# 데이터를 2차원으로 받아야할지 v

# depth가 0일 때 출발지 정해주기

# 마지막 깊이라면 sum += D[start]
# """

# """
# circuit = [
# [0, 10, 15, 20],
# [5, 0, 9, 10],
# [6, 13, 0, 12],
# [8, 8, 9, 0]]
# ]
# """
# # 재귀를 만들어서 붙여버릴까?


# def traveling_salesperson_problem(arr, result, visited, depth, origin):
#     if depth == 4:
#         print(result)
#         return
#     # visited = [F ,F ,F, F]
#     for i in range(4):
#         if depth == 0:
#             origin = i

#         if depth == 3:
#             result[depth] = arr[depth][origin]
#             traveling_salesperson_problem(arr, result, visited, depth + 1, origin)
#             # 마
#         elif not visited[i] and depth != i and arr[depth][i] != 0:
#             visited[i] = True
#             result[depth] = arr[depth][i]
#             traveling_salesperson_problem(arr, result, visited, depth + 1, origin)
#             visited[i] = False

#         # circuit[1] 도 들려야되고 1에서는 뭘돌려? 바로 circuit[1][i] 를 돌려야함 이게 depth=2
#         # circuit[2] 도 들려야해
#         # circuit[3] 도 들려야해

#     return


# circuit = [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]
# result = [0] * 4
# visited = [False] * 4

# traveling_salesperson_problem(circuit, result, visited, 0, 0)


# def traveling_salesperson_problem(arr, result, visited, depth, d_sum, start):
#     global count
#     if depth == 3:
#         d_sum += arr[depth][start]
#         print(d_sum)
#         print(result)
#         return

#     for i in range(len(arr)):  # 항상 모든원소를 순회
#         if arr[depth][i] == 0:  # 0이면 다음 요소
#             continue

#         if not visited[i]:  # 원소가 선택되지 않았더라면
#             visited[i] = True  # 해당원소 사용
#             d_sum += arr[depth][i]  # 더하기
#             result[depth] = arr[depth][i]
#             traveling_salesperson_problem(arr, result, visited, depth + 1, d_sum, start)
#             d_sum -= arr[depth][i]
#             visited[i] = False  # 해당원소 사용중지


# circuit = [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]
# visited = [False] * 4

# traveling_salesperson_problem(circuit, [0] * 4, visited, 0, 0, 0)
"""
4
T  T
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0

"""


import sys


min_cost = float("inf")


def traveling_salesperson_problem(arr, result, visited, depth, d_sum):
    global min_cost
    if depth == len(arr) - 1:
        if arr[result[depth - 1]][0] == 0:
            return  # 돌아갈 수 없으면 무효
        d_sum += arr[result[depth - 1]][0]
        min_cost = min(d_sum, min_cost)
        return

    for i in range(len(arr)):  # 항상 모든원소를 순회
        if not visited[i]:  # 원소가 선택되지 않았더라면
            cur_loca = result[depth - 1]
            print(f"depth = {depth}, {result[depth -1]}")
            if arr[cur_loca][i] == 0:
                continue
            visited[i] = True  # 해당원소 사용
            d_sum += arr[cur_loca][i]  # 더하기
            result[depth] = i
            traveling_salesperson_problem(arr, result, visited, depth + 1, d_sum)
            d_sum -= arr[cur_loca][i]
            visited[i] = False  # 해당원소 사용중지


N = int(input())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = [0] * len(data)
visited = [False] * len(data)
visited[0] = True


traveling_salesperson_problem(data, result, visited, 0, 0)
print(min_cost)
"""
0 2 9 3 4 7
1 0 6 8 2 5
4 3 0 1 7 2
5 2 8 0 3 6
3 5 1 4 0 9
7 4 2 3 6 0
"""


# def traveling_salesperson_problem(arr, result, visited, depth, d_sum):
#     global count
#     if depth == 4:
#         print(d_sum)
#         print(result)
#         return

#     for i in range(4):
#         if depth == 0:
#             start = i # 0을 유지할 수 있는게 뭘까..
#         if not visited[i]:
#             if arr[depth][i] == 0:
#                 continue
#             visited[i] = True
#             result[depth] = i
#             d_sum += arr[][i]
#             traveling_salesperson_problem(arr, result, visited, depth + 1, d_sum)
#             d_sum -= arr[][i]
#             visited[i] = False


# circuit = [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]
# visited = [False] * 4

# traveling_salesperson_problem(circuit, [0] * 4, visited, 0, 0)
