"""
( 1 2 )     ( 1 2 )
( 3 4 )     ( 3 4 )
"""

"""
패턴..

01+02, 01+13
23+02, 23+13

012+036, 012+147, 012+258
345+036, 345+147, 345+258
678+036, 678+147, 678+258
"""


import sys


def matrix_multiply(A, B):
    """
    두 행렬 A와 B를 곱하는 함수
    A: m x n 행렬
    B: n x p 행렬
    결과: m x p 행렬
    """
    row_A = len(A)
    col_A = len(A[0])
    col_B = len(B[0])

    result = [[0 for _ in range(col_B)] for _ in range(row_A)]
    for i in range(row_A):
        for j in range(col_B):
            for k in range(col_A):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % 1000

    # for row in range(len(result)):
    #     for col in range(len(result[0])):
    #         result[row][col] = result[row][col] % 1000

    return result


N, power = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    matrix.append(a)

memory = {}


def matrix_mod(matrix):
    """행렬의 모든 원소에 모듈로 연산 적용"""
    N = len(matrix)
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = matrix[i][j] % 1000
    return result


def matrix_power(matrix, power):
    if power in memory:
        return memory[power]  # 밑에서 검증안하고 위에서 하는것이 효율적

    if power == 1:  # 1일때 잘못계산함
        result = matrix_mod(matrix)
        memory[power] = result
        return result

    half = power // 2
    remainder = power - half

    # 코드 단축 가능 if else 안써도됨
    if half not in memory:
        memory[half] = matrix_power(matrix, half)
    left_matrix = memory[half]

    # 오른쪽 부분 계산
    if remainder not in memory:
        memory[remainder] = matrix_power(matrix, remainder)
    right_matrix = memory[remainder]

    # 최종 결과 계산 및 저장
    result = matrix_multiply(left_matrix, right_matrix)
    memory[power] = result
    return result


a = matrix_power(matrix, power)

for i in range(len(a)):
    print(" ".join(map(str, a[i])))
