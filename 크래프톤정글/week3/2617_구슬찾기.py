"""
가벼운 그래프
무거운 그래프

하나씩 생성

그래프에 간선을 따라가며 자기보다 무거운, 가벼운 정점 추가
"""

import sys


def assemble_graph(graph, i):
    visited = set()

    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(i)
    return len(visited) - 1


def count_reachable(graph, start):
    visited = set()
    count = 0

    def dfs(vertex):
        nonlocal count
        visited.add(vertex)
        if vertex != start:  # 시작점 제외
            count += 1

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return count


V, E = map(int, sys.stdin.readline().split())


over_graph = {}
under_graph = {}


for i in range(1, V + 1):  # 정점 생성
    over_graph[i] = []
    under_graph[i] = []

for _ in range(E):
    big, small = map(int, sys.stdin.readline().split())
    over_graph[small].append(big)
    under_graph[big].append(small)  # 간선 생성


count = 0
limit = (V // 2) + 1

for i in range(1, V + 1):
    heavy_count = assemble_graph(over_graph, i)
    light_count = assemble_graph(under_graph, i)

    if heavy_count >= limit or light_count >= limit:
        count += 1

print(count)

# 2 1
# 4 3
# 5 1
# 4 2


# def assemble_graph(graph, i):

#     start_n = i

#     def dfs(vertex, visited):
#         for ver in list(graph[vertex]):
#             if ver not in visited:
#                 visited.add(ver)
#                 if ver not in graph[start_n]:  # 중복 방지
#                     graph[start_n].append(ver)
#                 dfs(ver, visited)

#     visited = set([i])  # 시작 정점 포함

#     dfs(i, visited)
#     return len(graph[i])


# import sys
