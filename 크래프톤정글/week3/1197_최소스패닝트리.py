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

    def add_edge(self, vertex1, vertex2, cost=1):  # 무방향? 노방향!
        if not (vertex1 in self.adjacency_list and vertex2 in self.adjacency_list):
            return False
        self.adjacency_list[vertex1].append([vertex2, cost])
        self.adjacency_list[vertex2].append([vertex1, cost])
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

    def dfs_recursive(self, start):
        if start not in self.adjacency_list:
            return []
        visited = set()
        result = []

        def dfs(vertex):
            visited.add(vertex)
            result.append(vertex)

            for neighbor, _ in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start)
        return result

    def bfs(self, vertex):
        """
        큐에다가 넣고 순차적으로
        """
        if not vertex in self.adjacency_list:
            return []
        dq = deque()
        visited = set()
        visited.add(vertex)

        dq.append(vertex)

        result = []

        while len(dq) > 0:
            removed = dq.popleft()
            result.append(removed)
            for neighbor, cost in self.adjacency_list[removed]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dq.append(neighbor)
        return result

    def mst_prim(self):
        start = next(iter(self.adjacency_list))
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


g = Graph()
N, M = map(int, sys.stdin.readline().split())
for _ in range(M):
    v1, v2, edge = map(int, sys.stdin.readline().split())
    g.add_vertex(v1)
    g.add_vertex(v2)
    g.add_edge(v1, v2, edge)

mst = g.mst_prim()
total = sum([data[0] for data in mst])
print(total)


# ---


import heapq
import sys

graph = {}
V, E = map(int, sys.stdin.readline().split())

for i in range(1, V + 1):
    graph[i] = []

for _ in range(E):
    v1, v2, c = map(int, sys.stdin.readline().split())
    graph[v1].append((c, v2))
    graph[v2].append((c, v1))


def prim_mst():
    visited = set()
    visited.add(1)

    pq = []

    for c, n in graph[1]:
        heapq.heappush(pq, (c, n))

    sum_edge = []
    while pq and len(visited) < V:
        # 여기서 추가
        cost, cur_ver = heapq.heappop(pq)

        if cur_ver in visited:
            continue

        visited.add(cur_ver)
        sum_edge.append(cost)

        for n_cost, n_ver in graph[cur_ver]:
            if n_ver not in visited:
                heapq.heappush(pq, (n_cost, n_ver))

    print(sum(sum_edge))


prim_mst()
