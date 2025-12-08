import sys


def set_tile():
    N = int(sys.stdin.readline())
    if N <= 2:
        return N
    dp = [0] * (N + 1)

    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, N + 1):
        dp[i] = dp[i - 1] % 10007 + dp[i - 2] % 10007

    print(dp[N] % 10007)


set_tile()
