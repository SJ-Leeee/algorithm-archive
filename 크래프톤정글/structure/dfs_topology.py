def topological_sort_dfs(graph, V):
    visited = [False] * V  # O(V) 공간
    stack = []  # O(V) 공간

    def dfs(node):  # 재귀 스택: O(V) 공간
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)

    # 모든 정점에서 DFS                    # O(V + E) 시간
    for i in range(V):
        if not visited[i]:
            dfs(i)

    return stack[::-1]


"""
def topological_sort_dfs(graph, V):
    visited = [False] * V  # O(V) 공간
    stack = []  # O(V) 공간

    def dfs(node):  # 재귀 스택: O(V) 공간
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)

    # 모든 정점에서 DFS                    # O(V + E) 시간
    for i in range(V):
        if not visited[i]:
            dfs(i)

    return stack[::-1]

"""
