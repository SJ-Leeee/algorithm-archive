from collections import deque


def bfs_basic(graph, start):
    """
    기본 BFS 구현 - 모든 노드 방문

    Args:
        graph: 인접 리스트로 표현된 그래프
        start: 시작 노드

    Returns:
        방문 순서 리스트
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)
        print(f"방문: {current}")

        # 인접한 노드들을 큐에 추가
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def bfs_with_levels(graph, start):
    """
    레벨별 BFS - 각 노드의 거리 정보 포함

    Args:
        graph: 인접 리스트로 표현된 그래프
        start: 시작 노드

    Returns:
        (노드, 거리) 튜플들의 리스트
    """
    visited = set()
    queue = deque([(start, 0)])  # (노드, 거리)
    visited.add(start)
    result = []

    while queue:
        current, distance = queue.popleft()
        result.append((current, distance))
        print(f"방문: {current} (거리: {distance})")

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return result


def bfs_shortest_path(graph, start, target):
    """
    최단 경로 찾기 BFS

    Args:
        graph: 인접 리스트로 표현된 그래프
        start: 시작 노드
        target: 목표 노드

    Returns:
        최단 경로 리스트 (없으면 None)
    """
    if start == target:
        return [start]

    visited = set()
    queue = deque([(start, [start])])  # (현재 노드, 현재까지의 경로)
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        for neighbor in graph[current]:
            if neighbor not in visited:
                new_path = path + [neighbor]

                if neighbor == target:
                    return new_path

                visited.add(neighbor)
                queue.append((neighbor, new_path))

    return None


def bfs_level_order_traversal(graph, start):
    """
    레벨 순서대로 그룹화하여 반환

    Returns:
        레벨별로 그룹화된 노드들의 리스트
    """
    if not graph or start not in graph:
        return []

    visited = set()
    queue = deque([start])
    visited.add(start)
    levels = []

    while queue:
        level_size = len(queue)
        current_level = []

        # 현재 레벨의 모든 노드 처리
        for _ in range(level_size):
            current = queue.popleft()
            current_level.append(current)

            # 다음 레벨 노드들을 큐에 추가
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        levels.append(current_level)

    return levels


# 사용 예제
def demonstrate_bfs():
    # 예제 그래프
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    print("=== 기본 BFS ===")
    result = bfs_basic(graph, "A")
    print(f"방문 순서: {result}\n")

    print("=== 레벨별 BFS ===")
    level_result = bfs_with_levels(graph, "A")
    for node, distance in level_result:
        print(f"{node}: 거리 {distance}")
    print()

    print("=== 최단 경로 찾기 ===")
    path = bfs_shortest_path(graph, "A", "F")
    print(f"A에서 F까지의 최단 경로: {path}")
    print(f"최단 거리: {len(path) - 1}\n")

    print("=== 레벨 순서 순회 ===")
    levels = bfs_level_order_traversal(graph, "A")
    for i, level in enumerate(levels):
        print(f"레벨 {i}: {level}")


if __name__ == "__main__":
    demonstrate_bfs()

    from collections import deque
import heapq


def bidirectional_bfs(graph, start, target):
    """
    양방향 BFS - 시작점과 목표점에서 동시에 탐색

    Args:
        graph: 인접 리스트로 표현된 그래프
        start: 시작 노드
        target: 목표 노드

    Returns:
        최단 경로 (없으면 None)
    """
    if start == target:
        return [start]

    # 양방향 탐색을 위한 자료구조
    forward_queue = deque([start])
    backward_queue = deque([target])
    forward_visited = {start: [start]}
    backward_visited = {target: [target]}

    while forward_queue or backward_queue:
        # 전방 탐색
        if forward_queue:
            current = forward_queue.popleft()
            for neighbor in graph.get(current, []):
                if neighbor in backward_visited:
                    # 두 탐색이 만남!
                    forward_path = forward_visited[current]
                    backward_path = backward_visited[neighbor]
                    return forward_path + list(reversed(backward_path[:-1]))

                if neighbor not in forward_visited:
                    forward_visited[neighbor] = forward_visited[current] + [neighbor]
                    forward_queue.append(neighbor)

        # 후방 탐색 (역방향 그래프 필요)
        if backward_queue:
            current = backward_queue.popleft()
            # 역방향 그래프를 동적으로 생성
            for node in graph:
                if current in graph[node]:
                    if node in forward_visited:
                        # 두 탐색이 만남!
                        forward_path = forward_visited[node]
                        backward_path = backward_visited[current]
                        return forward_path + list(reversed(backward_path[:-1]))

                    if node not in backward_visited:
                        backward_visited[node] = [node] + backward_visited[current]
                        backward_queue.append(node)

    return None


def multi_source_bfs(graph, sources, target):
    """
    다중 시작점 BFS - 여러 시작점에서 동시에 탐색

    Args:
        graph: 인접 리스트로 표현된 그래프
        sources: 시작 노드들의 리스트
        target: 목표 노드

    Returns:
        (최단 거리, 최단 경로, 가장 가까운 시작점)
    """
    if target in sources:
        return 0, [target], target

    visited = {}
    queue = deque()

    # 모든 시작점을 큐에 추가
    for source in sources:
        queue.append((source, 0, [source], source))
        visited[source] = 0

    while queue:
        current, distance, path, original_source = queue.popleft()

        for neighbor in graph.get(current, []):
            if neighbor == target:
                return distance + 1, path + [neighbor], original_source

            if neighbor not in visited:
                visited[neighbor] = distance + 1
                queue.append(
                    (neighbor, distance + 1, path + [neighbor], original_source)
                )

    return float("inf"), None, None


def bfs_with_obstacles(grid, start, target, obstacles):
    """
    격자에서 장애물을 피하는 BFS

    Args:
        grid: (rows, cols) 크기의 격자
        start: (row, col) 시작 위치
        target: (row, col) 목표 위치
        obstacles: 장애물 위치들의 집합

    Returns:
        최단 경로 리스트 (없으면 None)
    """
    rows, cols = grid
    if start == target:
        return [start]

    visited = set()
    queue = deque([(start, [start])])
    visited.add(start)

    # 4방향 이동
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        (row, col), path = queue.popleft()

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            new_pos = (new_row, new_col)

            # 경계 체크
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                continue

            # 장애물 체크
            if new_pos in obstacles:
                continue

            # 방문 체크
            if new_pos in visited:
                continue

            new_path = path + [new_pos]

            if new_pos == target:
                return new_path

            visited.add(new_pos)
            queue.append((new_pos, new_path))

    return None


def bfs_connected_components(graph):
    """
    BFS를 이용한 연결 성분 찾기

    Args:
        graph: 인접 리스트로 표현된 그래프

    Returns:
        연결 성분들의 리스트
    """
    visited = set()
    components = []

    def bfs_component(start):
        component = []
        queue = deque([start])
        visited.add(start)

        while queue:
            current = queue.popleft()
            component.append(current)

            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return component

    for node in graph:
        if node not in visited:
            component = bfs_component(node)
            components.append(component)

    return components


def bfs_tree_diameter(tree, root):
    """
    BFS를 이용한 트리의 지름 구하기

    Args:
        tree: 트리를 나타내는 인접 리스트
        root: 루트 노드

    Returns:
        (지름, 지름을 이루는 두 노드)
    """

    def bfs_farthest(start):
        """시작점에서 가장 먼 노드와 거리 반환"""
        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)
        farthest_node = start
        max_distance = 0

        while queue:
            current, distance = queue.popleft()

            if distance > max_distance:
                max_distance = distance
                farthest_node = current

            for neighbor in tree.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        return farthest_node, max_distance

    # 1단계: 임의의 점에서 가장 먼 점 찾기
    node1, _ = bfs_farthest(root)

    # 2단계: 그 점에서 가장 먼 점 찾기 (이것이 지름)
    node2, diameter = bfs_farthest(node1)

    return diameter, (node1, node2)


# 사용 예제
def demonstrate_advanced_bfs():
    print("=== 양방향 BFS ===")
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "E"],
        "D": ["B", "F"],
        "E": ["C", "F"],
        "F": ["D", "E"],
    }

    path = bidirectional_bfs(graph, "A", "F")
    print(f"양방향 BFS 경로: {path}")

    print("\n=== 다중 시작점 BFS ===")
    distance, path, source = multi_source_bfs(graph, ["A", "B"], "F")
    print(f"가장 가까운 시작점: {source}")
    print(f"최단 거리: {distance}")
    print(f"최단 경로: {path}")

    print("\n=== 격자 BFS (장애물 회피) ===")
    grid = (5, 5)
    start = (0, 0)
    target = (4, 4)
    obstacles = {(1, 1), (1, 2), (2, 1), (3, 3)}

    path = bfs_with_obstacles(grid, start, target, obstacles)
    print(f"장애물을 피한 경로: {path}")

    print("\n=== 연결 성분 찾기 ===")
    disconnected_graph = {
        "A": ["B"],
        "B": ["A"],
        "C": ["D"],
        "D": ["C"],
        "E": ["F"],
        "F": ["E", "G"],
        "G": ["F"],
    }

    components = bfs_connected_components(disconnected_graph)
    print(f"연결 성분들: {components}")

    print("\n=== 트리 지름 구하기 ===")
    tree = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["E"],
    }

    diameter, endpoints = bfs_tree_diameter(tree, "A")
    print(f"트리의 지름: {diameter}")
    print(f"지름을 이루는 노드들: {endpoints}")


if __name__ == "__main__":
    demonstrate_advanced_bfs()

from collections import deque
import heapq


def bfs_early_termination(graph, start, target):
    """
    조기 종료를 통한 최적화
    목표를 찾으면 즉시 종료
    """
    if start == target:
        return [start]

    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()

        for neighbor in graph[current]:
            if neighbor not in visited:
                new_path = path + [neighbor]

                # 목표 발견 시 즉시 반환
                if neighbor == target:
                    return new_path

                visited.add(neighbor)
                queue.append((neighbor, new_path))

    return None


def bfs_with_pruning(graph, start, target, heuristic_func):
    """
    휴리스틱을 이용한 가지치기
    목표에서 너무 멀어지는 노드는 탐색하지 않음
    """
    if start == target:
        return [start]

    visited = {start}
    queue = deque([(start, [start], 0)])  # (노드, 경로, 거리)

    while queue:
        current, path, distance = queue.popleft()

        for neighbor in graph[current]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                new_distance = distance + 1

                if neighbor == target:
                    return new_path

                # 휴리스틱 함수로 가지치기
                if heuristic_func(neighbor, target) <= 10:  # 임계값
                    visited.add(neighbor)
                    queue.append((neighbor, new_path, new_distance))

    return None


def bfs_memory_optimized(graph, start, target):
    """
    메모리 최적화된 BFS
    경로를 저장하지 않고 부모만 추적
    """
    if start == target:
        return [start]

    visited = {start}
    queue = deque([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

                if neighbor == target:
                    # 경로 재구성
                    path = []
                    node = target
                    while node is not None:
                        path.append(node)
                        node = parent[node]
                    return list(reversed(path))

    return None


def bfs_level_optimization(graph, start, max_depth):
    """
    깊이 제한을 통한 최적화
    특정 깊이까지만 탐색
    """
    visited = {start}
    queue = deque([(start, 0)])  # (노드, 깊이)
    result = {0: [start]}

    while queue:
        current, depth = queue.popleft()

        if depth >= max_depth:
            continue

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_depth = depth + 1

                if new_depth not in result:
                    result[new_depth] = []
                result[new_depth].append(neighbor)

                queue.append((neighbor, new_depth))

    return result


def bfs_parallel_simulation(graph, start):
    """
    병렬 처리 시뮬레이션
    레벨별로 노드들을 동시에 처리
    """
    visited = {start}
    current_level = [start]
    level = 0
    all_levels = {0: [start]}

    while current_level:
        next_level = []

        # 현재 레벨의 모든 노드를 "병렬"로 처리
        for node in current_level:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_level.append(neighbor)

        if next_level:
            level += 1
            all_levels[level] = next_level
            current_level = next_level
        else:
            break

    return all_levels


def bfs_with_priority(graph, start, target, priority_func):
    """
    우선순위 기반 BFS
    인접 노드를 우선순위에 따라 정렬
    """
    if start == target:
        return [start]

    visited = {start}
    # 우선순위 큐 사용 (거리, 노드, 경로)
    queue = [(0, start, [start])]

    while queue:
        distance, current, path = heapq.heappop(queue)

        # 인접 노드들을 우선순위로 정렬
        neighbors = [
            (priority_func(neighbor, target), neighbor)
            for neighbor in graph[current]
            if neighbor not in visited
        ]
        neighbors.sort()

        for priority, neighbor in neighbors:
            if neighbor not in visited:
                new_path = path + [neighbor]

                if neighbor == target:
                    return new_path

                visited.add(neighbor)
                heapq.heappush(queue, (distance + 1, neighbor, new_path))

    return None


def benchmark_bfs_optimizations():
    """BFS 최적화 기법들의 성능 비교"""

    # 큰 그래프 생성
    def create_large_graph(size):
        graph = {}
        for i in range(size):
            graph[i] = []
            # 각 노드는 최대 4개의 인접 노드를 가짐
            for j in range(max(0, i - 2), min(size, i + 3)):
                if i != j:
                    graph[i].append(j)
        return graph

    large_graph = create_large_graph(1000)
    start, target = 0, 999

    # 휴리스틱 함수 (단순한 거리 추정)
    def simple_heuristic(node, target):
        return abs(node - target)

    # 우선순위 함수 (목표에 가까운 노드가 높은 우선순위)
    def priority_function(node, target):
        return abs(node - target)

    print("=== BFS 최적화 기법 비교 ===")

    # 1. 기본 BFS
    print("1. 기본 BFS")
    path1 = bfs_memory_optimized(large_graph, start, target)
    print(f"   경로 길이: {len(path1) if path1 else 'None'}")

    # 2. 조기 종료 BFS
    print("2. 조기 종료 BFS")
    path2 = bfs_early_termination(large_graph, start, target)
    print(f"   경로 길이: {len(path2) if path2 else 'None'}")

    # 3. 가지치기 BFS
    print("3. 가지치기 BFS")
    path3 = bfs_with_pruning(large_graph, start, target, simple_heuristic)
    print(f"   경로 길이: {len(path3) if path3 else 'None'}")

    # 4. 깊이 제한 BFS
    print("4. 깊이 제한 BFS (max_depth=10)")
    levels = bfs_level_optimization(large_graph, start, 10)
    print(f"   탐색한 레벨 수: {len(levels)}")

    # 5. 우선순위 BFS
    print("5. 우선순위 BFS")
    path5 = bfs_with_priority(large_graph, start, target, priority_function)
    print(f"   경로 길이: {len(path5) if path5 else 'None'}")


def demonstrate_optimization_principles():
    """최적화 원칙들 설명"""

    print("\n=== BFS 최적화 원칙들 ===")

    principles = [
        "1. 🎯 조기 종료 (Early Termination)",
        "   - 목표를 찾으면 즉시 탐색 중단",
        "   - 불필요한 노드 탐색 방지",
        "",
        "2. ✂️ 가지치기 (Pruning)",
        "   - 휴리스틱 함수로 유망하지 않은 경로 제거",
        "   - 탐색 공간 대폭 감소",
        "",
        "3. 💾 메모리 최적화",
        "   - 전체 경로 대신 부모 노드만 저장",
        "   - 필요할 때만 경로 재구성",
        "",
        "4. 📏 깊이/너비 제한",
        "   - 탐색 범위를 제한하여 시간 절약",
        "   - 근사해 허용 시 유용",
        "",
        "5. ⚡ 우선순위 기반 탐색",
        "   - 유망한 노드를 먼저 탐색",
        "   - A* 알고리즘의 기본 아이디어",
        "",
        "6. 🔄 양방향 탐색",
        "   - 시작점과 끝점에서 동시 탐색",
        "   - 탐색 공간을 절반으로 감소",
        "",
        "7. 🖥️ 병렬 처리",
        "   - 레벨별 노드들을 동시에 처리",
        "   - 멀티코어 환경에서 성능 향상",
    ]

    for principle in principles:
        print(principle)


if __name__ == "__main__":
    benchmark_bfs_optimizations()
    demonstrate_optimization_principles()


from collections import deque
import heapq


# 1. 다익스트라 알고리즘 (Dijkstra's Algorithm)
def dijkstra(graph, start):
    """
    다익스트라 알고리즘 - 가중치가 있는 그래프에서의 최단 경로
    BFS의 확장으로, 우선순위 큐를 사용
    """
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    parent = {node: None for node in graph}
    pq = [(0, start)]
    visited = set()

    while pq:
        current_distance, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        for neighbor, weight in graph[current]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current
                heapq.heappush(pq, (distance, neighbor))

    return distances, parent


# 2. A* 알고리즘
def a_star(graph, start, goal, heuristic):
    """
    A* 알고리즘 - 휴리스틱을 사용한 최적 경로 탐색
    BFS + 휴리스틱 함수
    """
    open_set = [(0, start)]
    came_from = {}
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0
    f_score = {node: float("inf") for node in graph}
    f_score[start] = heuristic(start, goal)

    while open_set:
        current_f, current = heapq.heappop(open_set)

        if current == goal:
            # 경로 재구성
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return list(reversed(path))

        for neighbor, weight in graph[current]:
            tentative_g = g_score[current] + weight

            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None


# 3. 벨만-포드 알고리즘 (Bellman-Ford Algorithm)
def bellman_ford(graph, start):
    """
    벨만-포드 알고리즘 - 음의 가중치가 있는 그래프에서의 최단 경로
    BFS의 개념을 확장하여 모든 간선을 반복적으로 완화
    """
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    parent = {node: None for node in graph}

    # V-1번 반복 (V는 정점의 수)
    for _ in range(len(graph) - 1):
        for node in graph:
            if distances[node] != float("inf"):
                for neighbor, weight in graph[node]:
                    if distances[node] + weight < distances[neighbor]:
                        distances[neighbor] = distances[node] + weight
                        parent[neighbor] = node

    # 음의 사이클 검출
    for node in graph:
        if distances[node] != float("inf"):
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    return None, None  # 음의 사이클 존재

    return distances, parent


# 4. 플로이드-워셜 알고리즘 (Floyd-Warshall Algorithm)
def floyd_warshall(graph):
    """
    플로이드-워셜 알고리즘 - 모든 쌍의 최단 경로
    BFS의 개념을 확장하여 모든 노드 쌍 간의 최단 거리 계산
    """
    nodes = list(graph.keys())
    n = len(nodes)

    # 거리 행렬 초기화
    dist = {}
    for i in nodes:
        dist[i] = {}
        for j in nodes:
            if i == j:
                dist[i][j] = 0
            else:
                dist[i][j] = float("inf")

    # 직접 연결된 간선들로 초기화
    for node in graph:
        for neighbor, weight in graph[node]:
            dist[node][neighbor] = weight

    # 플로이드-워셜 알고리즘
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# 5. 0-1 BFS (Deque를 이용한 최적화)
def zero_one_bfs(graph, start, target):
    """
    0-1 BFS - 가중치가 0 또는 1인 그래프에서의 최단 경로
    일반 BFS의 확장으로, deque의 양쪽 끝을 활용
    """
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    dq = deque([start])

    while dq:
        current = dq.popleft()

        if current == target:
            return distances[target]

        for neighbor, weight in graph[current]:
            new_distance = distances[current] + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

                if weight == 0:
                    dq.appendleft(neighbor)  # 가중치 0이면 앞쪽에 추가
                else:
                    dq.append(neighbor)  # 가중치 1이면 뒤쪽에 추가

    return distances[target] if target in distances else float("inf")


# 6. 다단계 BFS (Multi-level BFS)
def multi_level_bfs(graph, start, conditions):
    """
    다단계 BFS - 여러 조건을 만족하는 경로 찾기
    각 단계별로 다른 조건을 적용하는 BFS
    """
    queue = deque([(start, 0, [start])])  # (노드, 레벨, 경로)
    visited = {0: {start}}  # 레벨별 방문 노드

    for level in range(1, len(conditions) + 1):
        visited[level] = set()

    while queue:
        current, level, path = queue.popleft()

        if level >= len(conditions):
            return path  # 모든 조건을 만족하는 경로 발견

        condition = conditions[level]

        for neighbor in graph[current]:
            if condition(neighbor) and neighbor not in visited[level]:
                visited[level].add(neighbor)
                queue.append((neighbor, level + 1, path + [neighbor]))

    return None


# 7. 이분 그래프 검사 (Bipartite Graph Check)
def is_bipartite_bfs(graph):
    """
    BFS를 이용한 이분 그래프 판별
    """
    color = {}

    for start in graph:
        if start not in color:
            queue = deque([start])
            color[start] = 0

            while queue:
                current = queue.popleft()

                for neighbor in graph[current]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        return False  # 같은 색깔이면 이분 그래프가 아님

    return True


# 8. 레벨별 트리 순회 (Level-order Tree Traversal)
def level_order_traversal(root):
    """
    BFS를 이용한 레벨별 트리 순회
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_nodes = []

        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_nodes)

    return result


# 9. 최소 스패닝 트리 (Prim's Algorithm)
def prim_mst(graph, start):
    """
    프림 알고리즘 - BFS와 유사한 구조로 최소 스패닝 트리 구성
    """
    mst_edges = []
    visited = {start}
    edges = []

    # 시작 노드의 모든 간선을 우선순위 큐에 추가
    for neighbor, weight in graph[start]:
        heapq.heappush(edges, (weight, start, neighbor))

    while edges and len(visited) < len(graph):
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst_edges.append((u, v, weight))

            # 새로 추가된 노드의 간선들을 큐에 추가
            for neighbor, edge_weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (edge_weight, v, neighbor))

    return mst_edges


# 사용 예제 및 테스트
def demonstrate_derived_algorithms():
    """파생 알고리즘들의 동작 시연"""

    print("=== BFS 기반 파생 알고리즘들 ===")

    # 가중치 그래프 (인접 리스트, (노드, 가중치) 형태)
    weighted_graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2)],
        "E": [("C", 10), ("D", 2)],
    }

    print("1. 다익스트라 알고리즘")
    distances, parent = dijkstra(weighted_graph, "A")
    print(f"   A로부터의 최단 거리: {distances}")

    # 휴리스틱 함수 (단순한 예시)
    def manhattan_heuristic(node, goal):
        coords = {"A": (0, 0), "B": (1, 0), "C": (0, 1), "D": (2, 0), "E": (2, 1)}
        x1, y1 = coords[node]
        x2, y2 = coords[goal]
        return abs(x1 - x2) + abs(y1 - y2)

    print("\n2. A* 알고리즘")
    path = a_star(weighted_graph, "A", "E", manhattan_heuristic)
    print(f"   A에서 E까지의 A* 경로: {path}")

    # 0-1 가중치 그래프
    zero_one_graph = {
        "A": [("B", 0), ("C", 1)],
        "B": [("D", 1)],
        "C": [("D", 0), ("E", 1)],
        "D": [("E", 0)],
        "E": [],
    }

    print("\n3. 0-1 BFS")
    distance = zero_one_bfs(zero_one_graph, "A", "E")
    print(f"   A에서 E까지의 최단 거리: {distance}")

    # 이분 그래프 테스트
    bipartite_graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"],
    }

    print("\n4. 이분 그래프 검사")
    is_bip = is_bipartite_bfs(bipartite_graph)
    print(f"   그래프가 이분 그래프인가? {is_bip}")

    # 다단계 BFS 예제
    multi_graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [8, 9],
        5: [10, 11],
        6: [12, 13],
        7: [14, 15],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
        13: [],
        14: [],
        15: [],
    }

    # 조건들: 짝수 -> 홀수 -> 8보다 큰 수
    conditions = [
        lambda x: x % 2 == 0,  # 첫 번째 단계: 짝수
        lambda x: x % 2 == 1,  # 두 번째 단계: 홀수
        lambda x: x > 8,  # 세 번째 단계: 8보다 큰 수
    ]

    print("\n5. 다단계 BFS")
    multi_path = multi_level_bfs(multi_graph, 1, conditions)
    print(f"   다단계 조건을 만족하는 경로: {multi_path}")

    print("\n6. 프림 알고리즘 (최소 스패닝 트리)")
    mst = prim_mst(weighted_graph, "A")
    print(f"   최소 스패닝 트리 간선들: {mst}")
    total_weight = sum(weight for _, _, weight in mst)
    print(f"   총 가중치: {total_weight}")


def algorithm_comparison():
    """각 알고리즘의 특징과 용도 비교"""

    print(f"\n{'='*60}")
    print("BFS 기반 파생 알고리즘들의 특징")
    print(f"{'='*60}")

    algorithms = [
        ("다익스트라", "가중치 그래프 최단 경로", "O((V+E)logV)", "음이 아닌 가중치"),
        ("A*", "휴리스틱 기반 최적 경로", "O(b^d)", "게임 AI, 경로 찾기"),
        ("벨만-포드", "음의 가중치 허용", "O(VE)", "음의 사이클 검출"),
        ("플로이드-워셜", "모든 쌍 최단 경로", "O(V³)", "작은 그래프"),
        ("0-1 BFS", "0-1 가중치 특화", "O(V+E)", "특수한 경우 최적화"),
        ("이분 그래프 검사", "그래프 분할 가능성", "O(V+E)", "매칭 문제"),
        ("프림 MST", "최소 스패닝 트리", "O(ElogV)", "네트워크 설계"),
    ]

    print(f"{'알고리즘':<15} {'용도':<20} {'시간복잡도':<15} {'특징'}")
    print("-" * 70)
    for name, purpose, complexity, feature in algorithms:
        print(f"{name:<15} {purpose:<20} {complexity:<15} {feature}")


if __name__ == "__main__":
    demonstrate_derived_algorithms()
    algorithm_comparison()
