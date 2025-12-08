count = 0


def dfs(num, idx, depth, c_sum, N):
    global count
    print(c_sum)
    if c_sum == num and depth == N:
        count += 1
        return

    if depth == N:
        return

    for i in range(idx, 3):
        c_sum = c_sum + i + 1
        dfs(num, i, depth + 1, c_sum, N)
        c_sum = c_sum - i - 1


num = 4
N = 1

dfs(num, 0, 0, 0, 3)
print(count)
