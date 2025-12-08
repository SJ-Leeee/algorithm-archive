def unbounded_knapsack_dp(items, volume):
    dp = [0] * (volume + 1)  # [0, 0, 0, 0, 0, 0, ...]

    for v in range(volume + 1):  # 무게마다 돌 수 있다.
        for capacity, cost in items:
            # 만약 capacity가 v보다 무겁다면 할게 없음
            # 만약 capacity가 v보다 같거나 작으면
            if v >= capacity:
                # 여기서 음수가 나오는건 걸러지고, 아이템을 순회하기 때문에 가장 강한놈이 살아남는다
                dp[v] = max(dp[v], cost + dp[v - capacity])

    return dp


items = [(2, 3), (3, 4), (4, 5), (5, 8)]
volume = 8

# print(unbounded_knapsack_dp(items, volume))


def unbounded_knapsack_2d(items, volume):
    dp = [[0 for _ in range(volume + 1)] for _ in range(len(items) + 1)]
    items = [(0, 0)] + items
    for w in range(volume + 1):
        for i in range(1, len(items)):  # items = i-1 로 가야한다.
            dp[i][w] = dp[i - 1][w]

            if items[i][0] <= w:
                dp[i][w] = max(dp[i][w], items[i][1] + dp[i][w - items[i][0]])

    print(dp)


unbounded_knapsack_2d(items, volume)
