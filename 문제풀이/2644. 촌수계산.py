"""
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6

dfs 돌리면될것같은데
"""

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


# 모범답안
def dfs(graph, current, target, visited, depth):
    # 목표 지점 도달
    if current == target:
        return depth

    visited[current] = True

    # 인접한 모든 사람 탐색
    for next_person in graph[current]:
        if not visited[next_person]:
            result = dfs(graph, next_person, target, visited, depth + 1)
            if result != -1:  # 찾았으면 반환
                return result

    return -1  # 찾지 못함
