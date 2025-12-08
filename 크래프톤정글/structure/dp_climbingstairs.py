def climb_recur(n):
    if n <= 2:
        return n
    return climb_recur(n - 1) + climb_recur(n - 1)


n = 0
dp = [0] * (n + 1)
# memo OR memoization = {}


def climb_dp_td(n):
    if dp[n]:
        return dp[n]

    if n <= 2:
        return n

    dp[n] = climb_dp_td(n - 1) + climb_dp_td(n - 2)

    return dp[n]


def climb_dp_btu(n):
    # tabular OR tabulation = {}
    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
