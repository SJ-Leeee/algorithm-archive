import sys


def fibo(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    if n <= 1:
        return dp[n]

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


N = int(sys.stdin.readline())

result = fibo(N)
print(result)
