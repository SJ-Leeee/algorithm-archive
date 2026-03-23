def solution(brown, yellow):
    xy = brown + yellow
    col = 3
    while True:
        for row in range(3, col + 1):
            if col * row == xy and yellow == (col - 2) * (row - 2):
                return [col, row]
        col += 1
