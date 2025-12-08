# # 4 7
# # 6 13
# # 4 8
# # 3 6
# # 5 12

import sys


N, WEIGHT = map(int, sys.stdin.readline().split())

items = [(0, 0)]
for _ in range(N):
    weight, value = map(int, sys.stdin.readline().split())
    items.append((weight, value))
dp = [[0 for _ in range(WEIGHT + 1)] for _ in range(len(items))]

for i in range(len(items)):
    for w in range(WEIGHT + 1):
        item_weight = items[i][0]
        item_value = items[i][1]
        if item_weight > w:
            dp[i][w] = dp[i - 1][w]
        else:
            dp[i][w] = max(dp[i - 1][w], item_value + dp[i - 1][w - item_weight])

print(dp[N][WEIGHT])
