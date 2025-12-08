from collections import deque
import time
import sys


def comprehensive_comparison():
    """BFS와 DFS의 종합적인 비교"""

    print("=" * 70)
    print("🔍 BFS vs DFS 종합 비교")
    print("=" * 70)

    # 비교 테이블
    comparison_data = [
        ("특징", "BFS", "DFS"),
        ("자료구조", "큐(Queue)", "스택(Stack)/재귀"),
        ("탐색 방식", "레벨별(너비 우선)", "깊이 우선"),
        ("최단 경로", "✅ 보장 (무가중치)", "❌ 보장 안 됨"),
        ("메모리 사용", "O(w) - 너비", "O(h) - 높이"),
        ("완전성", "✅ 완전", "✅ 완전"),
        ("시간 복잡도", "O(V + E)", "O(V + E)"),
        ("구현 복잡도", "중간", "쉬움 (재귀)"),
    ]

    print(f"{'항목':<15} {'BFS':<25} {'DFS':<25}")
    print("-" * 65)
    for item, bfs_val, dfs_val in comparison_data:
        print(f"{item:<15} {bfs_val:<25} {dfs_val:<25}")

    print(f"\n{'='*70}")
    print("🎯 언제 어떤 알고리즘을 사용할까?")
    print("=" * 70)

    use_cases = [
        (
            "BFS가 최적인 상황",
            [
                "🎯 최단 경로가 중요한 문제",
                "📏 거리/레벨 기반 분석",
                "🌐 네트워크 라우팅",
                "🎮 게임에서 최단 이동",
                "🔍 목표가 시작점 근처에 있을 때",
                "📊 소셜 네트워크 분석",
            ],
        ),
        (
            "DFS가 최적인 상황",
            [
                "🧩 모든 해를 찾아야 할 때",
                "💾 메모리가 제한적인 환경",
                "🔄 백트래킹이 필요한 문제",
                "🏗️ 그래프 구조 분석",
                "🎯 목표가 깊은 곳에 있을 때",
                "📁 파일 시스템 탐색",
            ],
        ),
    ]

    for title, cases in use_cases:
        print(f"\n{title}:")
        for case in cases:
            print(f"  {case}")


def performance_benchmark():
    """실제 성능 벤치마크"""

    print(f"\n{'='*70}")
    print("⚡ 성능 벤치마크")
    print("=" * 70)

    def create_test_graphs():
        """테스트용 그래프들 생성"""

        # 1. 깊고 좁은 그래프 (DFS 유리)
        deep_narrow = {}
        for i in range(1000):
            deep_narrow[i] = [i + 1] if i < 999 else []

        # 2. 넓고 얕은 그래프 (BFS 유리)
        wide_shallow = {0: list(range(1, 501))}
        for i in range(1, 501):
            wide_shallow[i] = [501] if i <= 250 else []
        wide_shallow[501] = []

        # 3. 균형 잡힌 그래프
        balanced = {}
        for i in range(100):
            balanced[i] = []
            for j in range(max(0, i - 2), min(100, i + 3)):
                if i != j:
                    balanced[i].append(j)

        return deep_narrow, wide_shallow, balanced

    def bfs_simple(graph, start, target):
        queue = deque([start])
        visited = {start}
        nodes_visited = 0

        while queue:
            current = queue.popleft()
            nodes_visited += 1

            if current == target:
                return nodes_visited

            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return nodes_visited

    def dfs_simple(graph, start, target):
        visited = set()
        nodes_visited = 0

        def dfs(node):
            nonlocal nodes_visited
            if node in visited:
                return False

            visited.add(node)
            nodes_visited += 1

            if node == target:
                return True

            for neighbor in graph.get(node, []):
                if dfs(neighbor):
                    return True

            return False

        dfs(start)
        return nodes_visited

    deep_narrow, wide_shallow, balanced = create_test_graphs()

    test_cases = [
        ("깊고 좁은 그래프", deep_narrow, 0, 999),
        ("넓고 얕은 그래프", wide_shallow, 0, 501),
        ("균형 잡힌 그래프", balanced, 0, 99),
    ]

    print(f"{'그래프 타입':<20} {'BFS 방문수':<12} {'DFS 방문수':<12} {'더 효율적'}")
    print("-" * 60)

    for graph_type, graph, start, target in test_cases:
        try:
            bfs_visits = bfs_simple(graph, start, target)
            dfs_visits = dfs_simple(graph, start, target)

            if bfs_visits < dfs_visits:
                winner = "BFS"
            elif dfs_visits < bfs_visits:
                winner = "DFS"
            else:
                winner = "동일"

            print(f"{graph_type:<20} {bfs_visits:<12} {dfs_visits:<12} {winner}")
        except RecursionError:
            print(f"{graph_type:<20} {bfs_visits:<12} {'RecursionError':<12} {'BFS'}")


def memory_usage_comparison():
    """메모리 사용량 비교"""

    print(f"\n{'='*70}")
    print("💾 메모리 사용량 분석")
    print("=" * 70)

    def analyze_memory_usage():
        scenarios = [
            ("이진 트리 (깊이 20)", "BFS: 2^19 = ~500K 노드", "DFS: 20개 노드"),
            ("연결 리스트 (길이 1000)", "BFS: 1개 노드", "DFS: 1000개 노드"),
            ("완전 그래프 (노드 100)", "BFS: ~100개 노드", "DFS: ~100개 노드"),
            ("격자 그래프 (100x100)", "BFS: 너비에 따라 가변", "DFS: 경로 길이에 따라"),
        ]

        print(f"{'시나리오':<25} {'BFS 메모리':<20} {'DFS 메모리'}")
        print("-" * 65)

        for scenario, bfs_mem, dfs_mem in scenarios:
            print(f"{scenario:<25} {bfs_mem:<20} {dfs_mem}")

    analyze_memory_usage()


def algorithm_selection_guide():
    """알고리즘 선택 가이드"""

    print(f"\n{'='*70}")
    print("🧭 알고리즘 선택 가이드")
    print("=" * 70)

    decision_tree = """
    문제 분석 시작
    │
    ├─ 최단 경로가 중요한가?
    │  ├─ Yes → BFS 선택
    │  └─ No → 다음 질문으로
    │
    ├─ 모든 해를 찾아야 하는가?
    │  ├─ Yes → DFS + 백트래킹
    │  └─ No → 다음 질문으로
    │
    ├─ 메모리가 제한적인가?
    │  ├─ Yes → DFS 고려
    │  └─ No → 다음 질문으로
    │
    ├─ 그래프 구조 분석인가?
    │  ├─ Yes → DFS (사이클, 위상정렬 등)
    │  └─ No → 다음 질문으로
    │
    ├─ 목표가 어디에 있을 가능성이 높은가?
    │  ├─ 가까운 곳 → BFS
    │  ├─ 깊은 곳 → DFS
    │  └─ 모름 → BFS (안전한 선택)
    │
    └─ 구현 복잡도는?
       ├─ 간단함 선호 → DFS
       └─ 최적성 중요 → BFS
    """

    print(decision_tree)


def practical_examples():
    """실제 사용 예시"""

    print(f"\n{'='*70}")
    print("💡 실제 사용 예시")
    print("=" * 70)

    examples = [
        ("📱 GPS 네비게이션", "BFS", "최단 경로 찾기가 핵심"),
        ("🎮 게임 AI (체스)", "DFS", "모든 가능한 수를 분석"),
        ("🔍 웹 크롤러", "BFS", "레벨별로 체계적 탐색"),
        ("📁 파일 검색", "DFS", "디렉토리 구조가 깊음"),
        ("🌐 소셜 네트워크", "BFS", "친구 관계의 거리 분석"),
        ("🧩 스도쿠 해결", "DFS", "백트래킹으로 모든 경우 시도"),
        ("🚇 지하철 경로", "BFS", "최소 환승 경로"),
        ("🔄 사이클 검출", "DFS", "그래프 구조 분석"),
    ]

    print(f"{'응용 분야':<20} {'선택 알고리즘':<10} {'이유'}")
    print("-" * 55)

    for app, algo, reason in examples:
        print(f"{app:<20} {algo:<10} {reason}")


def final_recommendations():
    """최종 권장사항"""

    print(f"\n{'='*70}")
    print("🎯 최종 권장사항")
    print("=" * 70)

    recommendations = [
        "1. 🎯 확실하지 않다면 BFS를 선택하라",
        "   → 최단 경로를 보장하므로 안전한 선택",
        "",
        "2. 💾 메모리가 중요하다면 DFS를 고려하라",
        "   → 특히 깊고 좁은 구조에서 효과적",
        "",
        "3. 🧩 백트래킹이 필요하다면 DFS를 사용하라",
        "   → 조합/순열 문제의 표준 접근법",
        "",
        "4. 🔍 완전 탐색 시 문제 특성을 파악하라",
        "   → 목표의 위치와 그래프 구조 고려",
        "",
        "5. ⚡ 성능이 중요하다면 최적화 기법을 적용하라",
        "   → 양방향 탐색, 가지치기, 휴리스틱 활용",
        "",
        "6. 🛠️ 상황에 따라 하이브리드 접근법도 고려하라",
        "   → 문제의 다른 부분에 다른 알고리즘 적용",
    ]

    for rec in recommendations:
        print(rec)


if __name__ == "__main__":
    comprehensive_comparison()
    performance_benchmark()
    memory_usage_comparison()
    algorithm_selection_guide()
    practical_examples()
    final_recommendations()
