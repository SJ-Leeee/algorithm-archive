"""
1등부터해서 한번씩 싸악싸악
언제끝을내지? 싸악하고 얘는 통과
"""

# import sys


# N = int(sys.stdin.readline())
# for _ in range(N):
#     p_N = int(sys.stdin.readline())
#     people_grade = []
#     for _ in range(p_N):
#         r1, r2 = map(int, sys.stdin.readline().split())
#         people_grade.append((r1, r2))

#     people_grade.sort()

#     cnt = 1
#     min_interview = people_grade[0][1]
#     for i in range(1, len(people_grade)):
#         if people_grade[i][1] < min_interview:
#             cnt += 1
#             min_interview = people_grade[i][1]

#     print(cnt)

# 점프
"""


"""

import sys

goal, N = map(int, sys.stdin.readline().split())
small_stone = set()
for _ in range(N):
    s = int(sys.stdin.readline())
    small_stone.add(s)

max_speed = int((2 * N) ** 0.5) + 1
INF = float("inf")
dp = [[INF for _ in range(max_speed + 1)] for _ in range(goal + 1)]

if 2 not in small_stone:
    dp[2][1] = 1

for pos in range(2, goal + 1):
    if pos in small_stone:
        continue

    for speed in range(1, max_speed + 1):
        if dp[pos][speed] == INF:
            continue

        for n_speed in (speed - 1, speed, speed + 1):
            if n_speed <= 0:
                continue
            if n_speed > max_speed:
                continue

            n_pos = pos + n_speed

            if n_pos in small_stone:
                continue
            if n_pos > goal:
                continue

            dp[n_pos][n_speed] = min(dp[n_pos][n_speed], dp[pos][speed] + 1)

print(dp[goal])
