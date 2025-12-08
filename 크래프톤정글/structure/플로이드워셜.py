def floyd_warshall(graph):
    """
    플로이드-워셜 알고리즘으로 모든 정점 쌍 간의 최단 경로를 구함

    Args:
        graph: 2차원 리스트 (인접 행렬)
               INF는 연결되지 않은 간선을 의미

    Returns:
        dist: 최단 거리 행렬
        path: 경로 복원을 위한 행렬
    """
    INF = float("inf")
    n = len(graph)

    # 거리 행렬 초기화
    dist = [[INF] * n for _ in range(n)]
    path = [[-1] * n for _ in range(n)]

    # 초기 거리 설정
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != INF:
                dist[i][j] = graph[i][j]
                path[i][j] = i  # 직접 연결된 경우 이전 노드는 시작점

    # 플로이드-워셜 핵심 로직
    for k in range(n):  # 중간 경유점
        for i in range(n):  # 시작점
            for j in range(n):  # 도착점
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]  # 경로 갱신

    return dist, path


def get_path(path, start, end):
    """최단 경로를 복원하는 함수"""
    if path[start][end] == -1:
        return []

    result = []
    current = end

    while current != start:
        result.append(current)
        current = path[start][current]

    result.append(start)
    return result[::-1]


def detect_negative_cycle(dist):
    """음수 사이클 감지"""
    n = len(dist)
    for i in range(n):
        if dist[i][i] < 0:
            return True
    return False


# 사용 예제
if __name__ == "__main__":
    INF = float("inf")

    # 예제 그래프 (4개 정점)
    graph = [[0, 3, INF, 7], [8, 0, 2, INF], [5, INF, 0, 1], [2, INF, INF, 0]]

    print("원본 그래프:")
    for i, row in enumerate(graph):
        print(f"정점 {i}: {[x if x != INF else '∞' for x in row]}")

    # 플로이드-워셜 실행
    dist, path = floyd_warshall(graph)

    print("\n최단 거리 행렬:")
    for i in range(len(dist)):
        print(f"정점 {i}: {[x if x != INF else '∞' for x in dist[i]]}")

    # 음수 사이클 확인
    if detect_negative_cycle(dist):
        print("\n경고: 음수 사이클이 존재합니다!")

    # 특정 경로 출력
    start, end = 0, 2
    shortest_path = get_path(path, start, end)
    if shortest_path:
        print(
            f"\n정점 {start}에서 {end}까지의 최단 경로: {' -> '.join(map(str, shortest_path))}"
        )
        print(f"최단 거리: {dist[start][end]}")

    # 모든 쌍의 최단 거리 출력
    print("\n모든 정점 쌍의 최단 거리:")
    for i in range(len(dist)):
        for j in range(len(dist)):
            if i != j and dist[i][j] != INF:
                path_str = " -> ".join(map(str, get_path(path, i, j)))
                print(f"{i} → {j}: 거리 {dist[i][j]}, 경로 {path_str}")
