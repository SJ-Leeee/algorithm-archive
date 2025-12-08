"""
4 4 2 1

그래프 생성 후
"""

from collections import deque
import sys


class Graph:
    def __init__(self):
        self.injeop_list = {}

    def add_vertex(self, val):
        self.injeop_list[val] = []

    def add_edge(self, v1, v2):
        self.injeop_list[v1].append(v2)

    def bfs(self, start, K):
        result = []
        dq = deque()
        visited = set()

        dq.append((start, 0))
        visited.add(start)

        while len(dq) > 0:
            vertex, cnt = dq.popleft()
            if cnt == K:
                result.append(vertex)
            for neighbor in self.injeop_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dq.append((neighbor, cnt + 1))
        return result


V, E, K, S = map(int, sys.stdin.readline().split())
g = Graph()
for i in range(1, V + 1):
    g.add_vertex(i)

for _ in range(E):
    v1, v2 = map(int, sys.stdin.readline().split())
    g.add_edge(v1, v2)

ans = g.bfs(S, K)

if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)
