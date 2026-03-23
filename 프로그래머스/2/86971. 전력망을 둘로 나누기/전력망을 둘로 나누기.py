import copy


def solution(n, wires):
    answer = float("inf")
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for d1, d2 in wires:
        deep = copy.deepcopy(graph)
        deep[d1].remove(d2)
        deep[d2].remove(d1)

        cnt = dfs_recur(1, deep, n)
        diff = abs((n - cnt) - cnt)
        answer = min(answer, diff)

    return answer


def dfs_recur(start, graph, n):
    visited = [False] * (n + 1)
    cnt = 0

    def dfs(num):
        nonlocal cnt
        visited[num] = True
        cnt += 1
        for n_v in graph[num]:
            if not visited[n_v]:
                dfs(n_v)

    dfs(start)
    return cnt
