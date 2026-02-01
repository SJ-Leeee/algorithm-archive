# 4 7
# 20 15 10 17

# 적어도 7미터를 가져가기위한 높이의 최대값

import sys


def my_wood(woods, cutline):
    all_wood = 0

    for i in range(len(woods) - 1, -1, -1):  # 배열을 반대로 돌면서 나감
        cut_wood = woods[i] - cutline
        if cut_wood < 0:
            break
        all_wood += cut_wood

    return all_wood


N, M = map(int, sys.stdin.readline().split())
woods = list(map(int, sys.stdin.readline().split()))

woods.sort()


min_cut = woods[0]
max_cut = woods[-1]
answer = -1
while min_cut < max_cut:
    mid_cut = (min_cut + max_cut) // 2
    cutted_wood = my_wood(woods, mid_cut)
    # 5면 11
    # 6이면 8
    if cutted_wood == M:
        answer = mid_cut
        break
    elif cutted_wood > M:
        answer = mid_cut
        min_cut = mid_cut + 1
    else:
        max_cut = mid_cut

print(answer)

# 5 10
# 2 5 7 9 10
