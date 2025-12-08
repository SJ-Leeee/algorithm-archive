import sys


C, K = map(int, sys.stdin.readline().split())
dp = [1000000 for _ in range(K + 1)]
dp[0] = 0
coins = set()

for _ in range(C):
    coin = int(sys.stdin.readline())
    coins.add(coin)

coins = list(coins)
coins.sort()

for c in coins:
    for i in range(c, K + 1):
        dp[i] = min(dp[i], dp[i - c] + 1)

if dp[-1] == 1000000:
    print(-1)
else:
    print(dp[-1])
