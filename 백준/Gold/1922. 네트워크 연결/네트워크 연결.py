import sys


def find(parent, x):
    if parent[x] != x:  # 부모가 내가 아니면
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a, b = find(parent, a), find(parent, b)

    if a == b:
        return False  # 원래 같은 그룹

    parent[b] = a
    return True  # 이제 같은그룹


def kruskal(edges, n):
    # 간선 최소값 반환
    edges.sort(key=lambda x: x[2])  # 가중치로 정렬
    parent = list(range(n + 1))

    edge_count = 0
    total_count = 0

    for a, b, count in edges:
        if union(parent, a, b):  # 만약 다른그룹이었다면
            edge_count += 1
            total_count += count
            if edge_count == n - 1:  # 간선이 충분하다면
                break

    if edge_count < n - 1:
        return False

    return total_count


V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

edges = []
for _ in range(E):
    edge = list(map(int, sys.stdin.readline().split()))
    edges.append(edge)

ans = kruskal(edges, V)
print(ans)
