from collections import deque


def topology_khan(graph):

    result = []
    dq = deque()
    for i in range(1, len(graph) + 1):  # 1부터 N까지
        if indgree[i] == 0:
            dq.append(i)

    while dq:
        v = dq.popleft()
        result.append(v)
        for n in graph[v]:
            indgree[n] -= 1
            if indgree[n] == 0:
                dq.append(n)

    return result


graph = {}

for i in range(1, 5):
    graph[i] = []

indgree = [0] * (len(graph) + 1)


graph[2].append(4)
graph[1].append(4)
graph[2].append(3)
graph[1].append(3)
# 1 > 3 ,4
# 2 > 3, 4

indgree[3] += 2
indgree[4] += 2
a = topology_khan(graph)
print(a)
