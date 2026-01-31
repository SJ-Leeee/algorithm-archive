"""
컴퓨터의 개수 n개에 대해서 visit 배열 만들기
"""


def dfs(computers, com, visited):
    for idx, c in enumerate(com):  # [0,1,1]
        if c == 1 and not visited[idx]:  # 연결되어있고, 방문안했으면
            visited[idx] = True
            dfs(computers, computers[idx], visited)


def solution(n, computers):
    visited = [False] * n
    answer = 0

    for idx, i in enumerate(visited):
        if i == False:
            dfs(computers, computers[idx], visited)
            answer += 1

    return answer


def solution2(n, computers):
    parent = [i for i in range(n)]

    def find(n):
        if n != parent[n]:
            parent[n] = find(parent[n])
        return parent[n]

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                union(i, j)
    a = [find(i) for i in range(n)]

    return len(set(a))


solution2(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
