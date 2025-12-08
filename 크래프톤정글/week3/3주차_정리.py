"""
1991번 트리순회

전위 중위 후위 한 결과를 출력
"""

# import sys


# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# pre_list = []
# in_list = []
# post_list = []


# def pre_sort(node):
#     if not node:
#         return
#     pre_list.append(node.val)
#     pre_sort(node.left)
#     pre_sort(node.right)


# def in_sort(node):
#     if not node:
#         return
#     in_sort(node.left)
#     in_list.append(node.val)
#     in_sort(node.right)


# def post_sort(node):
#     if not node:
#         return
#     post_sort(node.left)
#     post_sort(node.right)
#     post_list.append(node.val)


# N = int(sys.stdin.readline())

# nodes = {}

# for _ in range(N):
#     p, l, r = sys.stdin.readline().strip().split()

#     p_n = TreeNode(p) if p not in nodes else nodes[p]

#     if l != ".":
#         l_n = TreeNode(l) if l not in nodes else nodes[l]
#         p_n.left = l_n
#     if r != ".":
#         r_n = TreeNode(r) if r not in nodes else nodes[r]
#         p_n.right = r_n

#     nodes[p] = p_n
#     nodes[l] = l_n
#     nodes[r] = r_n

# pre_sort(nodes["A"])
# in_sort(nodes["A"])
# post_sort(nodes["A"])

# print("".join(pre_list))
# print("".join(in_list))
# print("".join(post_list))


"""
5639

이진 검색 트리
"""


# import sys

# sys.setrecursionlimit(10000)


# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# class Tree:
#     def __init__(self):
#         self.root = None

#     def insert_node(self, node):
#         if not self.root:
#             self.root = node
#         else:
#             prev_node = None
#             cur_node = self.root

#             while cur_node:
#                 if cur_node.val > node.val:
#                     prev_node = cur_node
#                     cur_node = cur_node.left
#                 else:
#                     prev_node = cur_node
#                     cur_node = cur_node.right

#             if prev_node.val > node.val:
#                 prev_node.left = node
#             else:
#                 prev_node.right = node

#     def post_order(self):
#         result = []

#         def post_dfs(node):
#             if not node:
#                 return

#             post_dfs(node.left)
#             post_dfs(node.right)
#             result.append(node.val)

#         post_dfs(self.root)
#         return result


# tree = Tree()

# while True:
#     value = sys.stdin.readline().strip()

#     if not value:
#         break
#     # 처리 로직
#     value = int(value)
#     node = TreeNode(value)
#     tree.insert_node(node)

# a = tree.post_order()
# for i in a:
#     print(i)
# ---------

"""
1197
패닝 트리최소 스

프림알고리즘
"""


# from collections import deque
# import heapq
# import sys

# graph = {}
# V, E = map(int, sys.stdin.readline().split())

# for i in range(1, V + 1):
#     graph[i] = []

# for _ in range(E):
#     v1, v2, c = map(int, sys.stdin.readline().split())
#     graph[v1].append((c, v2))
#     graph[v2].append((c, v1))


# def prim_mst():
#     visited = set()
#     visited.add(1)

#     pq = []

#     for c, n in graph[1]:
#         heapq.heappush(pq, (c, n))

#     sum_edge = []
#     while pq and len(visited) < V:
#         # 여기서 추가
#         cost, cur_ver = heapq.heappop(pq)

#         if cur_ver in visited:
#             continue

#         visited.add(cur_ver)
#         sum_edge.append(cost)

#         for n_cost, n_ver in graph[cur_ver]:
#             if n_ver not in visited:
#                 heapq.heappush(pq, (n_cost, n_ver))

#     print(sum(sum_edge))


# prim_mst()


"""
1260 DFS와 BFS


"""


# from collections import deque
# import sys


# def dfs_iterative(graph, start):
#     """반복적 DFS - 스택 오버플로우 방지"""
#     visited = [False] * (V + 1)
#     result = []
#     stack = [start]

#     while stack:
#         node = stack.pop()
#         if not visited[node]:
#             visited[node] = True
#             result.append(node)
#             # 역순으로 추가해야 올바른 순서 보장
#             for neighbor in reversed(graph[node]):
#                 if not visited[neighbor]:
#                     stack.append(neighbor)

#     print(*result)


# def bfs(graph, root):
#     visited = [False] * (V + 1)
#     result = []
#     dq = deque()
#     dq.append(root)

#     while dq:
#         vertex = dq.popleft()

#         if visited[vertex]:
#             continue
#         visited[vertex] = True
#         result.append(vertex)
#         for neighbor in graph[vertex]:
#             if not visited[neighbor]:
#                 dq.append(neighbor)

#     print(*result)


# graph = {}
# V, E, S = map(int, sys.stdin.readline().split())

# for i in range(1, V + 1):
#     graph[i] = []

# for _ in range(E):
#     v1, v2 = map(int, sys.stdin.readline().split())
#     graph[v1].append(v2)
#     graph[v2].append(v1)


# for i in range(1, V + 1):
#     graph[i].sort()

# dfs_iterative(graph, S)
# bfs(graph, S)


"""
11724
연결요소의 개수
"""

# import sys


# graph = {}
# V, E = map(int, sys.stdin.readline().split())

# for i in range(1, V + 1):
#     graph[i] = []

# for _ in range(E):
#     v1, v2 = map(int, sys.stdin.readline().split())
#     graph[v1].append(v2)
#     graph[v2].append(v1)

# visited = set()


# def dfs(start):
#     stack = []
#     stack.append(start)
#     while stack:
#         v = stack.pop()

#         if v in visited:
#             continue

#         visited.add(v)

#         for n_v in graph[v]:
#             if n_v not in visited:
#                 stack.append(n_v)


# count = 0
# for i in range(1, V + 1):
#     if i not in visited:
#         dfs(i)
#         count += 1

# print(count)


"""
2606 바이러스

"""

# import sys


# graph = {}
# V = int(sys.stdin.readline())
# E = int(sys.stdin.readline())

# for i in range(1, V + 1):
#     graph[i] = []

# for _ in range(E):
#     v1, v2 = map(int, sys.stdin.readline().split())
#     graph[v1].append(v2)
#     graph[v2].append(v1)


# def dfs_recursion():
#     result = []
#     visited = [False] * (V + 1)

#     def dfs(v):
#         visited[v] = True
#         result.append(v)
#         for n_v in graph[v]:
#             if not visited[n_v]:
#                 dfs(n_v)

#     dfs(1)
#     print(len(result) - 1)


# dfs_recursion()


"""
11725 트리의 부모찾기

"""


# import sys

# sys.setrecursionlimit(100000)

# graph = {}
# V = int(sys.stdin.readline())

# for i in range(1, V + 1):
#     graph[i] = []

# for _ in range(V - 1):
#     v1, v2 = map(int, sys.stdin.readline().split())
#     graph[v1].append(v2)
#     graph[v2].append(v1)


# def dfs_recur():
#     previous = [False] * (V + 1)
#     visited = [False] * (V + 1)

#     def dfs(v):
#         visited[v] = True

#         for n_v in graph[v]:
#             if not visited[n_v]:
#                 previous[n_v] = v
#                 dfs(n_v)

#     dfs(1)
#     return previous


# a = dfs_recur()
# for i in range(2, V + 1):
#     print(a[i])

"""
1707 이분그래프

"""


# import sys

# sys.setrecursionlimit(100000)

# C = int(sys.stdin.readline())


# def dfs_recur(graph):
#     color = [None] * (len(graph) + 1)
#     visited = [False] * (len(graph) + 1)
#     result = True

#     def dfs(v, flag):
#         nonlocal result
#         color[v] = flag
#         visited[v] = True

#         for n_v in graph[v]:
#             if color[n_v] == flag:
#                 result = False
#             if not visited[n_v]:
#                 dfs(n_v, not flag)

#     for i in range(1, len(visited)):
#         if not visited[i]:
#             dfs(i, True)
#             if not result:
#                 return "NO"

#     return "YES"


# for _ in range(C):
#     graph = {}

#     V, E = map(int, sys.stdin.readline().split())
#     for i in range(1, V + 1):
#         graph[i] = []

#     for _ in range(E):
#         v1, v2 = map(int, sys.stdin.readline().split())
#         graph[v1].append(v2)
#         graph[v2].append(v1)

#     a = dfs_recur(graph)
#     print(a)

# key = list(graph.keys())

# for i in key:
#     res = dfs_recur(graph, i)

#     if res == "NO":
#         break
# print(res)

"""
21606 아침산책

케이스 분리 후 탐색문제
"""
import sys

sys.setrecursionlimit(200000)

graph = {}
N = int(sys.stdin.readline())
is_inside = [0] + list(map(int, sys.stdin.readline().strip()))
for i in range(1, N + 1):
    graph[i] = []

for _ in range(N - 1):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def morning_walk(graph, is_inside):
    visited = set()
    acc_cnt = 0
    temp_cnt = 0

    def dfs_out(start):
        nonlocal temp_cnt
        visited.add(start)

        for n_v in graph[start]:
            if is_inside[n_v]:  # 실내라면 숫자만 추가하고
                temp_cnt += 1
            else:  # 실외면 더 들어가자
                if n_v not in visited:
                    dfs_out(n_v)

    def dfs_in(start):
        nonlocal temp_cnt
        visited.add(start)

        for n_v in graph[start]:
            if is_inside[n_v] and n_v not in visited:  # 방문하지 않았고, 실내면 추가
                temp_cnt += 1
                dfs_in(n_v)
            # else: # 방문한적이 있거나, 실외면
            # temp_cnt = 0

    for i in range(1, len(is_inside)):
        if not is_inside[i] and i not in visited:  # 0이고 방문하지 않았던 실외
            dfs_out(i)
            acc_cnt += temp_cnt * (temp_cnt - 1)
            temp_cnt = 0
        if is_inside[i] and i not in visited:

            dfs_in(i)
            temp = temp_cnt if temp_cnt > 0 else 0
            acc_cnt += temp * 2
            temp_cnt = 0

    print(acc_cnt)
    # dfs


morning_walk(graph, is_inside)

"""
6
111011
1 3
2 3
3 4
4 5
4 6

"""
