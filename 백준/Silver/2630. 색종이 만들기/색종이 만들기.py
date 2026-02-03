import sys


N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white = 0
blue = 0


def is_same_color(paper, row, col, N):
    s_sum = 0
    for i in range(row, row + N):
        for j in range(col, col + N):
            s_sum += paper[i][j]

    if s_sum == N**2:
        return [True, 1]
    elif s_sum == 0:
        return [True, 0]
    else:
        return [False]


def paper_devide(paper, row, col, N):
    # 처음엔 paper, 0, 0, 8 로 옴
    global white, blue

    ret = is_same_color(paper, row, col, N)
    if ret[0] == True:
        if ret[1] == 1:
            blue += 1
        else:
            white += 1

        return

    half = N // 2
    paper_devide(paper, row, col + half, half)
    paper_devide(paper, row, col, half)
    paper_devide(paper, row + half, col, half)
    paper_devide(paper, row + half, col + half, half)


paper_devide(paper, 0, 0, N)

print(white)
print(blue)