"""
백트래킹
"""

# def is_possible(row, col):
#     for i in range(N):
#         if queens[row][i] == True:
#             return False

#         if queens[i][col] == True:
#             return False


#     for i in range(N):
#         for j in range(N):
#             if queens[i][j]:
#                 # ↘ 대각선
#                 if i - j == row - col:
#                     return False
#                 # ↙ 대각선
#                 if i + j == row + col:
#                     return False
#     return True

import sys


def is_possible(row, col):
    for i in range(N):
        if visited[row][i] == True:
            return False

        if visited[i][col] == True:
            return False

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                # ↘ 대각선
                if i - j == row - col:
                    return False
                # ↙ 대각선
                if i + j == row + col:
                    return False
    return True


def nqeen(depth):
    global count
    if depth == N:
        count += 1

        return

    for col in range(N):
        if is_possible(depth, col):
            visited[depth][col] = True
            nqeen(depth + 1)
            visited[depth][col] = False


count = 0

N = int(sys.stdin.readline())
visited = [[False] * N for _ in range(N)]
nqeen(0)
print(count)
