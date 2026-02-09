import sys


def find_family(start, end, graph, n):
    visited = [False] * (n + 1)
    relation_cnt = -1
    is_done = False

    #
    def dfs(visited, v, n):
        nonlocal relation_cnt, is_done
        visited[v] = True

        for nv in graph[v]:
            if not visited[nv] and not is_done:
                if nv == end:
                    is_done = True
                    relation_cnt = n + 1
                    break
                dfs(visited, nv, n + 1)

    dfs(visited, start, 0)

    return relation_cnt


V = int(sys.stdin.readline())
find_a, find_b = map(int, sys.stdin.readline().split())
family_chart = {}
for i in range(1, V + 1):
    family_chart[i] = []

E = int(sys.stdin.readline())
for _ in range(E):
    p, c = map(int, sys.stdin.readline().split())
    family_chart[p].append(c)
    family_chart[c].append(p)

ans = find_family(find_a, find_b, family_chart, V)
print(ans)
