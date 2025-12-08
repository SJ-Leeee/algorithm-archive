from collections import deque
import heapq
import sys


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):  # 무방향? 노방향!
        if not (vertex1 in self.adjacency_list and vertex2 in self.adjacency_list):
            return False
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)
        return True

    def remove_vertex(self, vertex):
        if not vertex in self.adjacency_list:
            return False
        while len(self.adjacency_list[vertex]) > 0:
            removed, cost = self.adjacency_list[vertex].pop()
            # item[0]이 정점 이름
            self.adjacency_list[removed] = [
                item for item in self.adjacency_list[removed] if item[0] != vertex
            ]

        del self.adjacency_list[vertex]

    def remove_edge(self, vertex1, vertex2):
        if not (vertex1 in self.adjacency_list and vertex2 in self.adjacency_list):
            return False

        self.adjacency_list[vertex1] = [
            item for item in self.adjacency_list[vertex1] if item[0] != vertex2
        ]
        self.adjacency_list[vertex2] = [
            item for item in self.adjacency_list[vertex2] if item[0] != vertex1
        ]
        return True

    def dfs_search(self, ver):
        if ver not in self.adjacency_list:
            return []
        result = []
        visited = set()

        def dfs(ver):

            result.append(ver)
            visited.add(ver)

            self.adjacency_list[ver].sort(key=lambda x: x)

            for v in self.adjacency_list[ver]:
                if v not in visited:
                    dfs(v)

        dfs(ver)

        return result

    def bfs_search(self, ver):
        if ver not in self.adjacency_list:
            return []

        dq = deque()
        dq.append(ver)
        result = []
        visited = set()
        visited.add(ver)

        while len(dq) > 0:
            ver = dq.popleft()
            result.append(ver)

            self.adjacency_list[ver].sort(key=lambda x: x)
            for v in self.adjacency_list[ver]:
                if v not in visited:
                    visited.add(v)
                    dq.append(v)
        return result

    def mst_prim(self, start):
        if not start in self.adjacency_list:
            return []
        """
        일단은 전부다 힙으로 만들어
        """
        mst = []
        visited = set()

        heap = [[0, start, start]]
        while heap and len(mst) < len(self.adjacency_list) - 1:
            cost, from_v, to_v = heapq.heappop(heap)

            if to_v in visited:
                continue

            visited.add(to_v)

            if from_v != to_v:
                mst.append([cost, from_v, to_v])

            for v, c in self.adjacency_list[to_v]:
                if v not in visited:
                    heapq.heappush(heap, [c, to_v, v])

        return mst


"""
4 5 1 정점의 개수, 간선의 개수, 시작할정점의 번호
1 2
1 3
1 4
2 4
3 4
"""

v, e, to_v = map(int, sys.stdin.readline().split())

g = Graph()

for i in range(1, v + 1):
    g.add_vertex(i)
for _ in range(e):
    v1, v2 = map(int, sys.stdin.readline().split())
    g.add_edge(v1, v2)

dfs_result = g.dfs_search(to_v)
bfs_result = g.bfs_search(to_v)

print(*dfs_result)
print(*bfs_result)
