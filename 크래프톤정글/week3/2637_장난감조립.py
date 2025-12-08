import sys


N = int(sys.stdin.readline())
E = int(sys.stdin.readline())

graph = {}
for i in range(1, N + 1):
    graph[i] = []

indgree = [0] * (N + 1)
for i in range(E):
    v1, v2, cnt = map(int, sys.stdin.readline().split())
    graph[v1].append((v2, cnt))
    indgree[v1] += 1

basic_parts = []

for i in range(1, N + 1):
    if not indgree[i]:
        basic_parts.append(i)

memo = {}


def memo_topol(part):
    if part in memo:
        return memo[part]

    if part in basic_parts:
        memo[part] = {}
        memo[part][part] = 1
        return memo[part]

    temp_memo = {}
    for n_v, count in graph[part]:
        result = memo_topol(n_v)
        for i in basic_parts:
            if i in result:
                if i not in temp_memo:
                    temp_memo[i] = result[i] * count
                else:
                    temp_memo[i] += result[i] * count

    memo[part] = temp_memo
    return memo[part]


result = memo_topol(N)
key = list(result.keys())
key.sort()
for k in key:
    print(k, result[k])
