"""
7
9
1 2 4
1 3 2
1 4 3
2 6 3
2 7 5
3 5 1
4 6 4
5 6 2
6 7 5
1 7
"""

# import heapq
# import sys


# V = int(sys.stdin.readline())
# E = int(sys.stdin.readline())

# graph = {}

# for i in range(1, V + 1):
#     graph[i] = []

# for _ in range(E):
#     v1, v2, cost = map(int, sys.stdin.readline().split())
#     graph[v1].append((v2, cost))

# S, G = map(int, sys.stdin.readline().split())


# def get():
#     result = []
#     max_cost = -1

#     def dfs(v, acc_cost, path):
#         nonlocal max_cost, result
#         if v == G:
#             re_path = path.copy()
#             if max_cost == acc_cost:
#                 result.append(re_path)
#             elif max_cost < acc_cost:
#                 max_cost = acc_cost
#                 result = [re_path]
#             return

#         for n_v, n_c in graph[v]:
#             path[n_v] = v
#             dfs(n_v, acc_cost + n_c, path)
#             del path[n_v]

#     dfs(S, 0, {})

#     all_pairs = []  # 모든 키-값 쌍을 set으로 변환하여 중복 제거
#     for d in result:
#         all_pairs.extend(d.items())

#     unique_pairs = list(set(all_pairs))
#     print(max_cost)
#     print(len(unique_pairs))


# get()


import heapq
import sys


V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

graph = {}

for i in range(1, V + 1):
    graph[i] = []

for _ in range(E):
    v1, v2, cost = map(int, sys.stdin.readline().split())
    graph[v1].append((cost, v2))

S, G = map(int, sys.stdin.readline().split())


def dijkstra(graph, start, end):
    nodes = []  # 우선순위 큐
    distances = {}  # 값을 저장할 객체
    previous = {}  # 이전 값 (경로확인할때) 저장할 객체
    result = []
    max_cost = -1
    injoep_keys = list(graph.keys())

    for vertex in injoep_keys:
        if vertex == start:
            distances[vertex] = 0
        else:
            distances[vertex] = float("-inf")  # 큰것으로만 갈 예정.

    heapq.heappush(nodes, (0, start))

    while nodes:
        cost, cur_node = heapq.heappop(nodes)
        cost = -cost

        if cost < distances[cur_node]:  # 현재코스트가 낮으면 안가도됨
            continue

        # 목표 도달하면 조기 종료
        if cur_node == end:
            re_path = previous.copy()
            if max_cost == acc_cost:
                result.append(re_path)
            elif max_cost < acc_cost:
                max_cost = cost
                result = [re_path]
            continue

        for n_cost, n_node in graph[cur_node]:
            acc_cost = cost + n_cost
            if distances[n_node] <= acc_cost:  # 내것이 같거나 높으면
                distances[n_node] = acc_cost  # 수정하고
                previous[n_node] = cur_node  # 이전거 정리하고
                heapq.heappush(nodes, (-acc_cost, n_node))
    print(max_cost)
    print(result)


dijkstra(graph, S, G)
