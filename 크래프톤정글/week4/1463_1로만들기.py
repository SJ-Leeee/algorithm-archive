"""
가능한 것에서 +1 중 작은것
"""

import sys


n = int(sys.stdin.readline())


def set1(n):
    if n <= 2:
        return n - 1
    dp = [10000] * (n + 1)
    dp[1] = 0
    dp[2] = 1

    for i in range(3, n + 1):
        div3 = dp[i // 3] if i % 3 == 0 else 10000
        div2 = dp[i // 2] if i % 2 == 0 else 10000
        dp[i] = min(div3 + 1, div2 + 1, dp[i - 1] + 1)

    return dp[n]


print(set1(n))
