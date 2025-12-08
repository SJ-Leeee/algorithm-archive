"""
점화식 f(n) = max(s(n) + s(n-1) + dp(n-3) , dp[n-2] + s[n])
"""

import sys


N = int(sys.stdin.readline())
s = []
dp = [0 for _ in range(N)]
for _ in range(N):
    stair = int(sys.stdin.readline())
    s.append(stair)


def stairs_dp():
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    dp[2] = s[2] + max(s[0], s[1])

    for i in range(3, N):
        dp[i] = max(s[i] + s[i - 1] + dp[i - 3], dp[i - 2] + s[i])


if N < 3:
    print(sum(s))
else:
    stairs_dp()
    print(dp[N - 1])
