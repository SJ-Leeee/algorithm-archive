import sys


blue = 0
white = 0


def count_paper(paper_list, r):
    global white, blue

    half = r // 2

    list_sum = 0
    for i in range(r):
        list_sum += sum(paper_list[i])

    if list_sum == 0:
        white += 1
        return

    if list_sum == r**2:
        blue += 1
        return

    half = r // 2

    q1 = [row[half:] for row in paper_list[:half]]
    q2 = [row[:half] for row in paper_list[:half]]
    q3 = [row[:half] for row in paper_list[half:]]
    q4 = [row[half:] for row in paper_list[half:]]

    count_paper(q1, half)
    count_paper(q2, half)
    count_paper(q3, half)
    count_paper(q4, half)

    return


N = int(sys.stdin.readline())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

count_paper(data, N)

print(white)
print(blue)


## gpt
## sum전체순회
## 현재코드는 순회하다가 종료


## 새로운 배열을 만들지 않고
## 원본배열에서 처리
def count_paper(paper_list, r, start_row=0, start_col=0):
    global white, blue

    # 첫 번째 원소로 전체가 같은지 확인
    first_value = paper_list[start_row][start_col]
    is_uniform = True

    # 조기 종료: 다른 값이 발견되면 바로 분할
    for i in range(start_row, start_row + r):
        for j in range(start_col, start_col + r):
            if paper_list[i][j] != first_value:
                is_uniform = False
                break
        if not is_uniform:
            break

    if is_uniform:
        if first_value == 0:
            white += 1
        else:
            blue += 1
        return

    # 분할정복 (새 리스트 생성하지 않고 인덱스만 전달)
    half = r // 2
    count_paper(paper_list, half, start_row, start_col)  # 좌상단
    count_paper(paper_list, half, start_row, start_col + half)  # 우상단
    count_paper(paper_list, half, start_row + half, start_col)  # 좌하단
    count_paper(paper_list, half, start_row + half, start_col + half)
