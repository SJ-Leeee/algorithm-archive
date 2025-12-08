import sys

# 25 10 5 1
N = int(sys.stdin.readline())
cost = [25, 10, 5, 1]
for _ in range(N):
    m = int(sys.stdin.readline())
    result = []
    for c in cost:
        result.append(m // c)
        m %= c
    print(*result)
