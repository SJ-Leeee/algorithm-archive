import sys


# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

N = int(sys.stdin.readline())
interview_graph = []
dp = [0] * (N + 1)
for _ in range(N):
    day, cost = map(int, sys.stdin.readline().split())
    interview_graph.append((day, cost))


for i in range(len(interview_graph) - 1, -1, -1):  # 길이는 7 idx=6
    itv_day, itv_cost = interview_graph[i]  # idx 6이고 1일이면 7에 접근 가능해야함
    end_day = i + itv_day  # 7
    if end_day > N:  # 8
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[end_day] + itv_cost)

print(max(dp))
