"""
dfs 안갈건데 확인은해보자

"""

import sys

sys.setrecursionlimit(100000)


def dfs_recur(adjacency_list):

    visited = {}

    def dfs(vertex, flag):
        visited[vertex] = flag

        for item in adjacency_list[vertex]:  # 여기있는 애들은 모두 반대플래그줘야돼
            if item in visited and visited[item] == flag:
                return False  # 걍 끝내버려야됨
            if item not in visited:
                result = dfs(item, not flag)  # 다음친구들은 반대 flag 줘야됨
                if not result:
                    return False

        return True

    for vertex in adjacency_list:
        if vertex not in visited:  # 새로운 연결 성분
            if not dfs(vertex, True):  # 이분 그래프 아니면
                return False

    return True


N = int(sys.stdin.readline())

for i in range(N):  # 두번 반복
    adjacency_list = {}  # 인접리스트 초기화
    v, e = map(int, sys.stdin.readline().split())  # 이번턴의 정점과 간선개수

    for j in range(1, v + 1):
        adjacency_list[j] = []  # 정점생성

    for k in range(e):
        v1, v2 = map(int, sys.stdin.readline().split())
        adjacency_list[v1].append(v2)
        adjacency_list[v2].append(v1)  # 간선 생성

    r_flag = dfs_recur(adjacency_list)

    if r_flag:
        print("YES")
    else:
        print("NO")


# while len(all_vertex) > 0:

#         flag, visited = dfs_recur(
#             adjacency_list, all_vertex[0]
#         )  # 여기까지 연결요소 한개
#         all_vertex = [v for v in all_vertex if v not in visited]  # 여기서 시간이 오래걸릴수도있음.
#         if not flag:
#             r_flag = False
