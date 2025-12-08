from collections import deque
import heapq
import sys


# def 위상정렬(graph, indgree):
#     # indgree가 0인것을 큐에 push하고 pop한것을 기반으로 indgree를 줄이고 다시 pop
#     """
#     indgree = {
#                 1: 0
#                 2: 1...
#             }
#     """
#     dq = deque()
#     result = []
#     for i in range(1, len(graph) + 1):
#         if indgree[i] == 0:
#             dq.append(i)

#     while dq:
#         node = dq.popleft()
#         result.append(node)

#         for next_node in graph[node]:
#             indgree[next_node] -= 1
#             if indgree[next_node] == 0:
#                 dq.append(next_node)

#     return result


# graph = {}

# for i in range(1, 5):
#     graph[i] = []

# indgree = [0] * (len(graph) + 1)


# graph[2].append(4)
# graph[1].append(4)
# graph[2].append(3)
# graph[1].append(3)
# # 1 > 3 ,4
# # 2 > 3, 4

# indgree[3] += 2
# indgree[4] += 2
# a = 위상정렬(graph, indgree)
# print(a)


# def dijkistra(graph, start, end):
#     # 출발지 도착지
#     previous = {}  # 이전값을 저장해둘 딕셔너리
#     min_table = {}  # 최소값을 저장해둘 딕셔너리
#     visited = set()  # 방문처리
#     pq = []  # 방문해야할 곳을 최소 힙으로 정렬

#     keys = list(graph.keys())

#     for i in keys:
#         if i == start:
#             min_table[i] = 0
#         else:
#             min_table[i] = float("inf")

#         previous[i] = None

#     heapq.heappush(pq, (0, start))
#     # 그래프는 가중그래프이고
#     while pq:
#         acc_cost, cur_node = heapq.heappop(pq)

#         if cur_node in visited:
#             continue
#         visited.add(cur_node)

#         if acc_cost > min_table[cur_node]:
#             continue

#         for cost, next_node in graph[cur_node]:
#             if cost + acc_cost < min_table[next_node]:
#                 previous[next_node] = cur_node
#                 min_table[next_node] = acc_cost + cost
#                 heapq.heappush(pq, (cost + acc_cost, next_node))
#     print(previous)
#     print(min_table)


# graph = {}
# V = int(sys.stdin.readline())
# E = int(sys.stdin.readline())

# for i in range(1, V + 1):
#     graph[i] = []

# for _ in range(E):
#     s_v, g_v, cost = map(int, sys.stdin.readline().split())
#     graph[s_v].append((cost, g_v))


# S, G = map(int, sys.stdin.readline().split())

# dijkistra(graph, S, G)


class Tri_node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Tri:
    def __init__(self):
        self.root = Tri_node()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Tri_node()
            node = node.children[char]
        node.is_end = True
        return

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return self.get_word_with_prefix(node, prefix)

    def get_word_with_prefix(self, node, prefix):  # 재귀함수
        words = []
        if node.is_end == True:  # 들어온 노드가 단어의 끝이라면 리턴
            words.append(prefix)

        for char, child_node in node.children.items():  # 하위 노드의 아이템들을 순회
            result = self.get_word_with_prefix(child_node, prefix + char)
            words.extend(result)

        return words
