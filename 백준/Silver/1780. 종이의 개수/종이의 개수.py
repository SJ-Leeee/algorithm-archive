"""
9

row = 0
col = 0
size = 9

new_size = 3
1구역 = row, col
2구역 = r, c+s
3구역 = r, c+s*2

4구역 = r+s, c
5구역 = r+s, c+s
6구역 = r+s, c+s*2

0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1
"""

"""
구역을 9개로 나눠야함
row = 0
col = 0
size = 3

1 1 1
0 0 0
1 1 1

탈출조건 N이 1일때
혹은 같은색상일때
"""
import sys


N = int(sys.stdin.readline())  # N은 3의 거듭제곱 형태
papers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

minus_one_cnt = 0
zero_cnt = 0
one_cnt = 0


def paper_helper(papers, row, col, size):
    global minus_one_cnt, zero_cnt, one_cnt

    origin_color = papers[row][col]

    for i in range(size):
        for j in range(size):
            if origin_color != papers[row + i][col + j]:
                return False

    if origin_color == -1:
        minus_one_cnt += 1
    elif origin_color == 0:
        zero_cnt += 1
    else:
        one_cnt += 1

    return True


def paper_recursive(papers, row, col, size):
    condition = paper_helper(papers, row, col, size)

    if condition:
        return

    new_size = size // 3
    for i in range(3):
        for j in range(3):
            paper_recursive(papers, row + i * new_size, col + j * new_size, new_size)


paper_recursive(papers, 0, 0, N)
print(minus_one_cnt)
print(zero_cnt)
print(one_cnt)