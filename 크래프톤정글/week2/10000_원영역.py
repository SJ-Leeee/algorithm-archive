import sys


N = int(sys.stdin.readline())
circles = []
for _ in range(N):
    x, r = map(int, sys.stdin.readline().split())
    circles.append([True, x - r, r, r])
    circles.append([False, x + r, r, r])

circles.sort(key=lambda x: (x[1], x[0], -x[2] if x[0] else x[2]))
# 첫번째 인자: 괄호의 여부 (여는 괄호:True)
# 두번째 인자: 위치 값 x
# 세번째 인자: 반지름 길이

stack = []
count = 1
for circle in circles:
    if circle[0] == True:  # 여는괄호면 무조건 삽입
        stack.append(circle)
    else:  # False라면 무조건 True는 존재함
        removed = stack.pop()
        add_count = 1

        if len(stack) != 0:  # Pop하고도 존재한다면

            origin_r = removed[3]
            flag, position_x, width, r = stack[-1]
            stack[-1] = [
                True,
                circle[1],
                width - origin_r,
                r,
            ]  # 닫는 위치의 x로 위치를 옮김

        if removed[2] == 0:
            add_count += 1

        count += add_count

print(count)
