"""
3 3
1 2 3
4 5 6
7 8 9

필요한 함수
1. 쪼개는 함수
2. 곱하는 함수
3. 모듈로 연산 함수
일단
A^n = A^2/n * A^2/n
A^n = A^2/n * A^2/n * A

똑같은 수니까 메모제이션 필요함
모듈러연산은 언제하지? 매번해도됨
"""

import sys

N, EXP = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
matrix_product_memo = {}


def matrix_modular(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            m[i][j] = m[i][j] % 1000
    return m


def matrix_product(a, b):
    n = len(a)  # N*N 행렬
    result = [[0] * n for _ in range(n)]
    # result[0][0] = A (0,0) * B (0,0) + A(0,1) * B (1,0)
    # result[0][1] = A (0,0) * B (0,1) + A(0,1) * B (1,1)
    # result[1][0] = A (1,0) * B (0,0) + A(1,1) * B (1,0)
    # result[1][1] = A (1,0) * B (0,1) + A(1,1) * B (1,1)

    # result[0][0] = A (0,0) * B (0,0) + A(0,1) * B (1,0) + A(0,2) * B(2,0)
    for row in range(n):  # A의 행
        for col in range(n):  # B의 열
            for elem in range(n):  # 각 원소
                result[row][col] += a[row][elem] * b[elem][col]

    return matrix_modular(result)


def matrix_divde(exp, matrix):
    # 탈출조건
    if exp in matrix_product_memo:
        # n차원 행렬형태
        return matrix_product_memo[exp]

    if exp == 1:
        return matrix_modular(matrix)

    # 나누기
    half = matrix_divde(exp // 2, matrix)
    if exp % 2 == 0:  # 짝수라면
        matrix_product_memo[exp] = matrix_product(half, half)
    else:  # 홀수라면
        matrix_product_memo[exp] = matrix_product(matrix_product(half, half), matrix)

    return matrix_product_memo[exp]


answer = matrix_divde(EXP, matrix)
for i in answer:
    print(*i)