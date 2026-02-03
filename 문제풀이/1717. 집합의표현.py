"""
7 9
0 1 3
1 1 7
0 7 6
0 1 7
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""

# import sys

# sys.setrecursionlimit(10**7)


# def dfs_recursive(v, find_v):
#     memo = set()

#     def dfs(v, find_v, memo):
#         memo.add(v)

#         for nv in graph[v]:
#             if nv == find_v:
#                 return "YES"
#             if nv not in memo:
#                 dfs(nv, find_v, memo)

#     if v == find_v:
#         return "YES"

#     ans = dfs(v, find_v, memo)
#     return ans if ans == "YES" else "NO"


# V, M = map(int, sys.stdin.readline().split())
# graph = {}
# for i in range(1, V + 1):
#     graph[i] = []

# for _ in range(M):
#     cmd, v1, v2 = map(int, sys.stdin.readline().split())
#     if cmd == 0:
#         if v1 == v2:
#             continue
#         ans = dfs_recursive(v1, v2)
#         if ans == "NO":
#             graph[v1].append(v2)
#             graph[v2].append(v1)
#     else:
#         ans = dfs_recursive(v1, v2)
#         print(ans)


"""
7 9
0 1 3
1 1 7
0 7 6
0 1 7
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""


# def dfs_recursive(v, find_v):
#     memo = set()

#     def dfs(v, find_v, memo):
#         memo.add(v)

#         for nv in graph[v]:
#             if nv == find_v:
#                 return "YES"
#             if nv not in memo:
#                 ans = dfs(nv, find_v, memo)
#                 if ans == "YES":
#                     return "YES"
#         return "NO"

#     if v == find_v:
#         return "YES"

#     ans = dfs(v, find_v, memo)
#     return ans if ans == "YES" else "NO"


# from collections import deque
# import sys

# V, M = map(int, sys.stdin.readline().split())
# graph = {}
# for i in range(1, V + 1):
#     graph[i] = []

# for _ in range(M):
#     cmd, v1, v2 = map(int, sys.stdin.readline().split())

#     # print(graph)
#     if cmd == 0:
#         if v1 == v2:
#             continue
#         graph[v1].append(v2)
#         graph[v2].append(v1)
#     else:  # 1이면 bfs 돌려야함
#         dq = deque()
#         if v1 == v2:
#             print("YES")
#             continue
#         visited = [False] * (V + 1)
#         ans = "NO"

#         dq.append(v1)  # bfs시작

#         while dq:
#             v = dq.popleft()

#             if visited[v]:  # 이미 방문했으면 넘어감
#                 continue

#             visited[v] = True
#             if v == v2:  # 찾으면 끝
#                 ans = "YES"
#                 break

#             for nv in graph[v]:

#                 if not visited[nv]:
#                     dq.append(nv)
#         print(ans)

"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""

import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 루트에 직접 연결
    return parent[x]


def union(x1, x2):
    a, b = find(x1), find(x2)
    if a != b:
        parent[b] = a


V, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(V + 1)]
for _ in range(M):
    cmd, v1, v2 = map(int, sys.stdin.readline().split())

    if cmd == 0:
        union(v1, v2)
    else:
        ans = "YES" if find(v1) == find(v2) else "NO"
        print(ans)
