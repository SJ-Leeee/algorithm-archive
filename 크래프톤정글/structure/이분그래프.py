from collections import deque


def is_bipartite_bfs(graph, n):
    """
    BFS를 이용한 이분그래프 판별
    시간복잡도: O(V + E)
    """
    color = [-1] * n  # -1: 미방문, 0: 그룹A, 1: 그룹B

    for start in range(n):
        if color[start] == -1:  # 아직 방문하지 않은 컴포넌트
            queue = deque([start])
            color[start] = 0  # 시작점을 그룹 A로 설정

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        # 인접 노드를 다른 그룹으로 색칠
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # 같은 그룹에 속한 노드끼리 연결됨 → 이분그래프 아님
                        return False, None

    # 두 그룹으로 분리
    group_a = [i for i in range(n) if color[i] == 0]
    group_b = [i for i in range(n) if color[i] == 1]

    return True, (group_a, group_b)


def is_bipartite_dfs(graph, n):
    """
    DFS를 이용한 이분그래프 판별
    시간복잡도: O(V + E)
    """
    color = [-1] * n

    def dfs(node, c):
        color[node] = c

        for neighbor in graph[node]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:
                return False
        return True

    for i in range(n):
        if color[i] == -1:
            if not dfs(i, 0):
                return False, None

    group_a = [i for i in range(n) if color[i] == 0]
    group_b = [i for i in range(n) if color[i] == 1]

    return True, (group_a, group_b)


def check_odd_cycle(graph, n):
    """
    홀수 길이 사이클 검출로 이분그래프 판별
    """
    color = [-1] * n

    def dfs(node, c, parent):
        color[node] = c

        for neighbor in graph[node]:
            if neighbor == parent:
                continue

            if color[neighbor] == -1:
                if not dfs(neighbor, 1 - c, node):
                    return False
            elif color[neighbor] == c:
                # 홀수 길이 사이클 발견
                return False
        return True

    for i in range(n):
        if color[i] == -1:
            if not dfs(i, 0, -1):
                return False
    return True


# 사용 예시
if __name__ == "__main__":
    # 테스트 케이스 1: 이분그래프
    graph1 = [
        [1, 3],  # 0번 노드의 인접 리스트
        [0, 2],  # 1번 노드의 인접 리스트
        [1, 3],  # 2번 노드의 인접 리스트
        [0, 2],  # 3번 노드의 인접 리스트
    ]

    # 테스트 케이스 2: 이분그래프가 아님 (삼각형)
    graph2 = [[1, 2], [0, 2], [0, 1]]  # 0번 노드  # 1번 노드  # 2번 노드

    print("=== 테스트 케이스 1 ===")
    is_bip1, groups1 = is_bipartite_bfs(graph1, 4)
    print(f"이분그래프 여부: {is_bip1}")
    if is_bip1:
        print(f"그룹 A: {groups1[0]}")
        print(f"그룹 B: {groups1[1]}")

    print("\n=== 테스트 케이스 2 ===")
    is_bip2, groups2 = is_bipartite_bfs(graph2, 3)
    print(f"이분그래프 여부: {is_bip2}")

    print("\n=== DFS 방법 테스트 ===")
    is_bip3, groups3 = is_bipartite_dfs(graph1, 4)
    print(f"DFS 결과: {is_bip3}")

    print("\n=== 홀수 사이클 검출 ===")
    print(f"그래프1 홀수 사이클 없음: {check_odd_cycle(graph1, 4)}")
    print(f"그래프2 홀수 사이클 있음: {not check_odd_cycle(graph2, 3)}")
