import sys


N = int(sys.stdin.readline())
canvas = [[" "] * (2 * N - 1) for _ in range(N)]


def draw(row, col, size):
    if size == 3:
        canvas[row][col + 2] = "*"
        canvas[row + 1][col + 1] = "*"
        canvas[row + 1][col + 3] = "*"

        for i in range(5):
            canvas[row + 2][col + i] = "*"
        return
    half = size // 2
    draw(row, col + half, half)
    draw(row + half, col, half)
    draw(row + half, col + size, half)


draw(0, 0, N)
for row in canvas:
    print("".join(row))