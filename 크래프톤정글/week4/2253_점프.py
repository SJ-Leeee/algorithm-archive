"""

뛴거리 n, 현재 i

f(i + n - 1) = cnt+1
f(i + n) = cnt+1
f(i + n + 1) = cnt+1

jump[i + n - 1] = n - 1
jump[i + n] = n
jump[i + n + 1] = n + 1

"""

"""
f(x) = f(x - n + 1) + 1
f(x) = f(x - n) + 1
f(x) = f(x - n - 1) + 1
"""


# import sys


# def jump_cl(goal, dp, jump):

#     for i in range(1, goal + 1):
#         if dp[i] == -1:
#             continue

#         n = jump[i]

#         if i + n - 1 > goal or i + n > goal or i + n + 1 > goal:
#             continue

#         dp[i + n - 1] = min(dp[i + n - 1], dp[i] + 1)
#         dp[i + n] = min(dp[i] + 1, dp[i + n])
#         dp[i + n + 1] = min(dp[i] + 1, dp[i + n + 1])

#         jump[i + n - 1] = min(jump[i + n - 1], n - 1)
#         jump[i + n] = min(n, jump[i + n])
#         jump[i + n + 1] = min(n + 1, jump[i + n + 1])
#     print(dp)


# G, B = map(int, sys.stdin.readline().split())

# dp = [100000] * (G + 1)
# jump = [1000] * (G + 1)

# dp[1] = 1
# jump[1] = 0
# for _ in range(B):
#     b = int(sys.stdin.readline())
#     dp[b] = False

# jump_cl(G, dp, jump)


import sys


def jump_stone():
    pos, S = map(int, sys.stdin.readline().split())
    small_stone = set()

    for _ in range(S):
        small_s = int(sys.stdin.readline())
        small_stone.add(small_s)
    INF = float("inf")

    max_speed = int((2 * pos) ** 0.5) + 1

    dp = [[INF for _ in range(max_speed + 1)] for _ in range(pos + 1)]
    # 스피드는 1부터하자

    if 2 not in small_stone:
        dp[2][1] = 1
    # 고려해봐야할 경우

    for i in range(2, pos + 1):
        if i in small_stone:  # small_stone 이라면
            continue

        for speed in range(1, max_speed + 1):
            if dp[i][speed] == INF:
                continue

            for next_speed in [speed - 1, speed, speed + 1]:
                if next_speed <= 0:
                    continue
                if next_speed > max_speed:
                    continue

                next_pos = i + next_speed

                if next_pos in small_stone:
                    continue
                if next_pos > pos:
                    continue

                dp[next_pos][next_speed] = min(
                    dp[next_pos][next_speed], dp[i][speed] + 1
                )

    return min(dp[pos]) if min(dp[pos]) != INF else -1


a = jump_stone()
print(a)
