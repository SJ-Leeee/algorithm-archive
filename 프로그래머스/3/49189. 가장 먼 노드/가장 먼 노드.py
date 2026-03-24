import heapq


def dijkstra(graph, start):
    n = len(graph)  # 6
    distance = [float("inf")] * (n + 1)
    distance[start] = 0

    pq = [(0, start)]  # (거리, 노드)

    while pq:
        dist, node = heapq.heappop(pq)

        # 이미 처리된 노드면 스킵
        if dist > distance[node]:
            continue

        for neighbor in graph[node]:
            new_dist = dist + 1

            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distance


def solution(n, edge):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []

    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)

    root = dijkstra(graph, 1)
    root[0] = -1

    return len([x for x in root if x == max(root)])