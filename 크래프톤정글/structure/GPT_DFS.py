def dfs_iterative(graph, start):
    """
    스택을 이용한 반복적 DFS 구현

    Args:
        graph: 인접 리스트로 표현된 그래프
        start: 시작 노드

    Returns:
        방문 순서 리스트
    """
    visited = set()
    stack = [start]
    result = []

    while stack:
        # 스택에서 노드를 꺼냄
        current = stack.pop()

        if current not in visited:
            # 현재 노드 방문
            visited.add(current)
            result.append(current)
            print(f"방문: {current}")

            # 인접한 노드들을 스택에 추가 (역순으로 추가하여 왼쪽부터 방문)
            for neighbor in reversed(graph[current]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


def dfs_recursive(graph, start, visited=None):
    """
    재귀를 이용한 DFS 구현

    Args:
        graph: 인접 리스트로 표현된 그래프
        start: 시작 노드
        visited: 방문한 노드들을 저장하는 집합

    Returns:
        방문 순서 리스트
    """
    if visited is None:
        visited = set()

    result = []

    # 현재 노드 방문
    visited.add(start)
    result.append(start)
    print(f"방문: {start}")

    # 인접한 노드들을 재귀적으로 방문
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result


# 사용 예제
if __name__ == "__main__":
    # 그래프를 인접 리스트로 표현
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    print("=== 재귀 방식 DFS ===")
    result = dfs_recursive(graph, "A")
    print(f"방문 순서: {result}")


def dfs_with_path(graph, start, target):
    """
    경로를 추적하는 DFS

    Args:
        graph: 인접 리스트로 표현된 그래프
        start: 시작 노드
        target: 목표 노드

    Returns:
        시작점에서 목표점까지의 경로 (없으면 None)
    """
    visited = set()
    stack = [(start, [start])]  # (현재 노드, 현재까지의 경로)

    while stack:
        current, path = stack.pop()

        if current == target:
            return path

        if current not in visited:
            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None


# 사용 예제
if __name__ == "__main__":
    # 그래프를 인접 리스트로 표현
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    print("=== 반복적 DFS ===")
    result = dfs_iterative(graph, "A")
    print(f"방문 순서: {result}")

    print("\n=== 경로 탐색 DFS ===")
    path = dfs_with_path(graph, "A", "F")
    print(f"A에서 F까지의 경로: {path}")


def dfs_optimized_bitmask(graph, start, n):
    """
    비트마스크를 이용한 메모리 효율적인 DFS

    Args:
        graph: 인접 리스트 (노드는 0부터 n-1까지의 정수)
        start: 시작 노드
        n: 총 노드 개수
    """
    visited = 0  # 비트마스크로 방문 상태 관리
    stack = [start]
    result = []

    while stack:
        current = stack.pop()

        # 현재 노드가 방문되지 않았다면
        if not (visited & (1 << current)):
            visited |= 1 << current  # 방문 표시
            result.append(current)

            # 인접 노드들을 스택에 추가
            for neighbor in reversed(graph[current]):
                if not (visited & (1 << neighbor)):
                    stack.append(neighbor)

    return result


def dfs_with_pruning(graph, start, condition_func):
    """
    조건에 따른 가지치기를 적용한 DFS

    Args:
        graph: 인접 리스트
        start: 시작 노드
        condition_func: 노드가 탐색할 가치가 있는지 판단하는 함수
    """
    visited = set()
    stack = [start]
    result = []

    while stack:
        current = stack.pop()

        if current not in visited and condition_func(current):
            visited.add(current)
            result.append(current)

            # 조건을 만족하는 인접 노드만 스택에 추가
            for neighbor in graph[current]:
                if neighbor not in visited and condition_func(neighbor):
                    stack.append(neighbor)

    return result


def dfs_early_termination(graph, start, target_func):
    """
    목표 조건을 만족하면 조기 종료하는 DFS

    Args:
        graph: 인접 리스트
        start: 시작 노드
        target_func: 목표 조건을 확인하는 함수

    Returns:
        목표 노드를 찾으면 해당 노드, 없으면 None
    """
    visited = set()
    stack = [start]

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)

            # 목표 조건을 만족하면 즉시 반환
            if target_func(current):
                return current

            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return None


# 사용 예제
if __name__ == "__main__":
    # 숫자 노드 그래프 (0~5)
    numeric_graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1, 5], 5: [2, 4]}

    print("=== 비트마스크 DFS ===")
    result = dfs_optimized_bitmask(numeric_graph, 0, 6)
    print(f"방문 순서: {result}")

    print("\n=== 가지치기 DFS (짝수 노드만) ===")
    even_only = lambda x: x % 2 == 0
    result = dfs_with_pruning(numeric_graph, 0, even_only)
    print(f"짝수 노드만 방문: {result}")

    print("\n=== 조기 종료 DFS (값이 4인 노드 찾기) ===")
    find_four = lambda x: x == 4
    result = dfs_early_termination(numeric_graph, 0, find_four)
    print(f"찾은 노드: {result}")
