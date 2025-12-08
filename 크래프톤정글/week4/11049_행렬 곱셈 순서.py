"""
3
5 3
3 2
2 6

점화식
result(2) = 1*2 행렬곱
result(2) = 2*3 행렬곱 ...

dp[2] = min(결과1 + 결과2, 결과2 + 결과1)
"""

# matrix_product = []


import sys


def matrix_count():
    N = int(sys.stdin.readline())
    matrix = []
    for _ in range(N):
        R, C = map(int, sys.stdin.readline().split())
        matrix.append((R, C))

    memo = [[-1 for _ in range(N)] for _ in range(N)]

    def matrix_helper(x, y, matrix):
        if memo[x][y] != -1:
            return memo[x][y]
        if x >= y:
            return 0

        mn = float("inf")
        for k in range(x, y):
            mn = min(
                mn,
                matrix_helper(x, k, matrix)
                + matrix_helper(k + 1, y, matrix)
                + matrix[x][0] * matrix[k][1] * matrix[y][1],
            )
        memo[x][y] = mn
        return memo[x][y]

    mn = matrix_helper(0, N - 1, matrix)
    print(mn)


matrix_count()
# 참고 https://www.youtube.com/watch?v=Tdl6VP4bS90&t=1602s
