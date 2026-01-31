from collections import deque
import sys


def left_lotation(num):
    num_dq_cpy = deque(num_dq)
    cnt = 0
    while True:
        tmp = num_dq_cpy.popleft()
        if tmp == num:
            break
        num_dq_cpy.append(tmp)
        cnt += 1
    return cnt, num_dq_cpy


def right_lotation(num):
    num_dq_cpy = deque(num_dq)
    cnt = 0
    while True:
        tmp = num_dq_cpy.pop()
        cnt += 1
        if tmp == num:
            break
        num_dq_cpy.appendleft(tmp)
    return cnt, num_dq_cpy


N, M = map(int, sys.stdin.readline().split())
find_num_list = list(map(int, sys.stdin.readline().split()))
find_num_list.reverse()
num_dq = deque(range(1, N + 1))

cnt = 0
while find_num_list:
    find_n = find_num_list.pop()

    cnt2, num_dq_2 = left_lotation(find_n)

    cnt3, num_dq_3 = right_lotation(find_n)

    if cnt2 > cnt3:
        num_dq = num_dq_3
        cnt += cnt3
    else:
        num_dq = num_dq_2
        cnt += cnt2

print(cnt)
