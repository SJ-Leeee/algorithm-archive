# ACAYKP
# CAPCAK

import sys


X = sys.stdin.readline().strip()
Y = sys.stdin.readline().strip()


def lcs(x, y):
    x = " " + x
    y = " " + y

    m = len(x)
    n = len(y)

    dp = [[0 for _ in range(n)] for _ in range(m)]
    s_dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                s_dp[i][j] = 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                s_dp[i][j] = (
                    2 if dp[i][j - 1] < dp[i - 1][j] else 3
                )  # x가 크면 2, y가 같거나 크면 3

    return dp[m - 1][n - 1], s_dp


def lcs_string(m, n, s_dp, x):
    if m == 0 or n == 0:
        return ""

    if s_dp[m][n] == 1:
        return lcs_string(m - 1, n - 1, s_dp, x) + x[m]
    elif s_dp[m][n] == 2:
        return lcs_string(m - 1, n, s_dp, x)
    else:
        return lcs_string(m, n - 1, s_dp, x)


num, s_dp = lcs(X, Y)

a = lcs_string(len(X), len(Y), s_dp, " " + X)

print(num)
print(a)
