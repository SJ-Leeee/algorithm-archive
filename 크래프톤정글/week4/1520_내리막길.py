import sys

sys.setrecursionlimit(10**5)
R, C = map(int, sys.stdin.readline().split())
location = []
dp = [[-1 for _ in range(C)] for _ in range(R)]

for _ in range(R):
    line = list(map(int, sys.stdin.readline().split()))
    location.append(line)

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_recur(row, col):
    if row == 0 and col == 0:
        return 1

    if dp[row][col] != -1:
        return dp[row][col]

    dp[row][col] = 0  # 초기화!

    for dr, dc in direct:
        n_r, n_c = row + dr, col + dc

        if 0 <= n_r < R and 0 <= n_c < C:
            if location[row][col] < location[n_r][n_c]:
                # dp[n_r][n_c] = find_recur(n_r, n_c)
                dp[row][col] += find_recur(n_r, n_c)

    return dp[row][col]


print(find_recur(R - 1, C - 1))


# dq = deque()
# dq.append((0, 0))

# while dq:
#     row, col = dq.popleft()

#     for dr, dc in direct:
#         n_r, n_c = row + dr, col + dc

#         if dp[n_r][n_c]:
#             dp[r][c] += dp[n_r][n_c]

#         if 0 <= n_r < R and 0 <= n_c < C:
#             if location[row][col] > location[n_r][n_c]:
#                 dp[n_r][n_c] += 1
#                 dq.append((n_r, n_c))

# print(dp[R - 1][C - 1])
