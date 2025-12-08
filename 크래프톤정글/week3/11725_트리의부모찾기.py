from collections import deque
import sys

sys.setrecursionlimit(10000)


def dfs_parents(child_vertex):

    s_v = list(adjacency_list.keys())[0]
    visited = set()

    def dfs(vertex, parent):
        if vertex == child_vertex:
            return parent  # ← 찾았으면 즉시 반환

        visited.add(vertex)

        for neighbor in adjacency_list[vertex]:
            if neighbor not in visited:
                result = dfs(neighbor, vertex)
                if result is not None:  # ← 결과가 있으면 즉시 반환
                    return result

        return None  # 못 찾았으면 None

    pa = dfs(s_v, None)
    return pa


def dfs_recur():
    s_v = list(adjacency_list.keys())[0]
    result = []
    visited = set()

    def dfs(vertex, parents):
        result.append([vertex, parents])
        visited.add(vertex)

        for item in adjacency_list[vertex]:
            if item not in visited:
                dfs(item, vertex)

    dfs(s_v, None)
    return result


adjacency_list = {}

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    adjacency_list[i] = []

for _ in range(N - 1):
    v1, v2 = map(int, sys.stdin.readline().split())
    adjacency_list[v1].append(v2)
    adjacency_list[v2].append(v1)

# for i in range(2, N + 1):
#     i_parents = dfs_parents(i)
#     print(i_parents)

re = dfs_recur()
re.sort(key=lambda x: x[0])

for i in range(1, len(re)):
    print(re[i][1])
