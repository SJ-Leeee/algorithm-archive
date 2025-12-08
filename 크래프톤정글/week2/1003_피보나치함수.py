# 피보나치 함수


import sys


# a = fibo(7)
# print(a)


memo = {}


def count_fibo(n):
    if n == 0:
        return (1, 0)
    if n == 1:
        return (0, 1)

    if n in memo:
        return memo[n]
    else:
        zero_1, one_1 = count_fibo(n - 1)
        zero_2, one_2 = count_fibo(n - 2)
        memo[n] = (zero_1 + zero_2, one_1 + one_2)
        return memo[n]


N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    a = count_fibo(num)
    print(a[0], a[1])
