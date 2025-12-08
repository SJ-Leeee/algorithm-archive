from collections import deque
import heapq
import sys


class Graph:
    def __init__(self):
        self.injeop_list = {}

    def add_vertex(self, val):
        self.injeop_list[val] = []

    def add_edge(self, v1, v2, cost):
        self.injeop_list[v1].append((cost, v2))

    def dfs_recursive(self, start, goal):
        keys = self.injeop_list.keys()
        visited = {}  # 다 존재한다면 그냥 여기보다 낮으면 이어가면 되잔항.
        memo = {}  # 추가: (노드, 현재비용) -> 최소비용

        for i in keys:
            visited[i] = float("inf")

        def dfs(s, g, c_sum):
            if s in memo and memo[s] <= c_sum:
                return
            memo[s] = c_sum

            for nxt, cost in self.injeop_list[s]:
                if nxt == g:
                    visited[g] = min(visited[g], c_sum + cost)
                elif visited[nxt] > c_sum + cost:
                    visited[nxt] = c_sum + cost
                    dfs(nxt, g, c_sum + cost)

        dfs(start, goal, 0)

        return visited

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

    def dijkstra(self, start, end):
        nodes = []  # 우선순위 큐
        distances = {}  # 값을 저장할 객체
        previous = {}  # 이전 값 (경로확인할때) 저장할 객체

        injoep_keys = list(self.injeop_list.keys())

        for vertex in injoep_keys:
            if vertex == start:
                distances[vertex] = 0
            else:
                distances[vertex] = float("inf")

            previous[vertex] = None

        heapq.heappush(nodes, (0, start))

        while nodes:
            cost, cur_node = heapq.heappop(nodes)
            # 핵심 수정: 이미 더 좋은 경로로 처리됐으면 스킵
            if cost > distances[cur_node]:
                continue

            # 목표 도달하면 조기 종료
            if cur_node == end:
                return distances[end]
            for n_cost, next_node in self.injeop_list[cur_node]:
                acc_cost = cost + n_cost
                if distances[next_node] > acc_cost:
                    distances[next_node] = acc_cost
                    previous[next_node] = cur_node
                    heapq.heappush(nodes, (acc_cost, next_node))
        return distances[end]


V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
g = Graph()
for i in range(1, V + 1):
    g.add_vertex(i)

for _ in range(E):
    v1, v2, c = map(int, sys.stdin.readline().split())
    g.add_edge(v1, v2, c)

S, G = map(int, sys.stdin.readline().split())

a = g.dijkstra(S, G)

print(a)
