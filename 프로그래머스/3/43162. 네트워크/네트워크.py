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