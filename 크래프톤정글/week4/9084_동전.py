import sys


def coin_count(num, coins):
    dp = [0] * (num + 1)
    dp[0] = 1
    for coin in coins:  # 1,2

        for i in range(num + 1):
            if i >= coin:
                dp[i] += dp[i - coin]

    return dp[-1]


N = int(sys.stdin.readline())

for _ in range(N):
    M = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    num = int(sys.stdin.readline())
    a = coin_count(num, coins)
    print(a)
