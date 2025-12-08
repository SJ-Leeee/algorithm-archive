# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7


# 1번부터 7번까지 생성
# 6번 순회해서 결합


from collections import deque
import sys


def dfs_recur():
    s_v = list(adjancy_list.keys())[0]
    result = []
    visited = set()

    def dfs(vertex):
        result.append(vertex)
        visited.add(vertex)

        for item in adjancy_list[vertex]:
            if item not in visited:
                dfs(item)

    dfs(s_v)
    return result


def bfs(s_v):
    if s_v == None:
        s_v = list(adjancy_list.keys())[0]

    dq = deque()
    result = []
    visited = set()
    dq.append(s_v)
    visited.add(s_v)

    while len(dq) > 0:
        removed = dq.popleft()

        result.append(removed)
        for item in adjancy_list[removed]:
            if item not in visited:
                visited.add(item)
                dq.append(item)

    return result


adjancy_list = {}

N = int(sys.stdin.readline())

M = int(sys.stdin.readline())
for i in range(1, N + 1):

    adjancy_list[i] = []

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    adjancy_list[v1].append(v2)
    adjancy_list[v2].append(v1)

re1 = dfs_recur()

print(len(re1) - 1)
