# 5 7

# 0 0 0 0 0 0 0
# 0 2 4 5 3 0 0
# 0 3 0 2 5 2 0
# 0 7 6 2 4 0 0
# 0 0 0 0 0 0 0

"""
배열과 인접리스트를 같이 생성
인접리스트의 간선개수로 count 조정
순회로 연결요소가 몇개인지 찾기
"""

from collections import deque
import sys


def bfs(s_v):
    if s_v == None:
        s_v = list(injeop_list.keys())[0]

    dq = deque()
    result = []
    visited = set()
    dq.append(s_v)
    visited.add(s_v)

    while len(dq) > 0:
        removed = dq.popleft()

        result.append(removed)
        for item in injeop_list[removed]:
            if item not in visited:
                visited.add(item)
                dq.append(item)

    return result


R, C = map(int, sys.stdin.readline().split())
# visited = [[False for _ in range(C)] for _ in range(R)]
ice_map = []
injeop_list = {}

for _ in range(R):  # ice map 만들기 2차원
    data = list(map(int, sys.stdin.readline().split()))
    ice_map.append(data)

for i in range(R):
    for j in range(C):  # ice map을 기반으로 그래프 생성
        if ice_map[i][j] != 0:
            injeop_list[(i, j)] = []
            for r, c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if ice_map[i + r][j + c] != 0:
                    injeop_list[(i, j)].append((i + r, j + c))

count = 0
while len(injeop_list) > 0:
    key_list = list(injeop_list.keys())  # 모든 키
    all_keys = bfs(None)  # bfs로 탐색 아무거나
    if len(key_list) != len(all_keys):  # 비교
        break

    for r, c in key_list:  # 감소
        discount = 4 - len(injeop_list[(r, c)])
        ice_map[r][c] -= discount

    for r, c in key_list:  # 삭제
        if ice_map[r][c] <= 0:
            while len(injeop_list[(r, c)]) > 0:
                e_r, e_c = injeop_list[(r, c)].pop()
                injeop_list[(e_r, e_c)] = [
                    item for item in injeop_list[(e_r, e_c)] if item != (r, c)
                ]

            del injeop_list[(r, c)]
    count += 1

if len(injeop_list) == 0:
    print(0)
else:
    print(count)

# {
#     (1, 1): [(1, 2), (2, 1)],
#     (1, 2): [(1, 3), (1, 1)],
#     (1, 3): [(1, 4), (2, 3), (1, 2)],
#     (1, 4): [(2, 4), (1, 3)],
#     (2, 1): [(3, 1), (1, 1)],
#     (2, 3): [(2, 4), (3, 3), (1, 3)],
#     (2, 4): [(2, 5), (3, 4), (2, 3), (1, 4)],
#     (2, 5): [(2, 4)],
#     (3, 1): [(3, 2), (2, 1)],
#     (3, 2): [(3, 3), (3, 1)],
#     (3, 3): [(3, 4), (3, 2), (2, 3)],
#     (3, 4): [(3, 3), (2, 4)],
# }


# {
#     (1, 2): [(1, 3)],
#     (1, 3): [(1, 4), (2, 3), (1, 2)],
#     (1, 4): [(2, 4), (1, 3)],
#     (2, 1): [(3, 1)],
#     (2, 3): [(2, 4), (3, 3), (1, 3)],
#     (2, 4): [(3, 4), (2, 3), (1, 4)],
#     (3, 1): [(3, 2), (2, 1)],
#     (3, 2): [(3, 3), (3, 1)],
#     (3, 3): [(3, 4), (3, 2), (2, 3)],
#     (3, 4): [(3, 3), (2, 4)],
# }
