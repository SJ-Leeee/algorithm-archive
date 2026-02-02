import sys


N = int(sys.stdin.readline())


cnt = 0


def hanoi_1(n, start, end, mid):
    global cnt
    if n == 1:
        cnt += 1
        return
    hanoi_1(n - 1, start, mid, end)
    cnt += 1
    hanoi_1(n - 1, mid, end, start)


def hanoi_2(n, start, end, mid):
    if n == 1:
        print(start, end)
        return
    hanoi_2(n - 1, start, mid, end)
    print(start, end)
    hanoi_2(n - 1, mid, end, start)


hanoi_1(N, 1, 3, 2)
print(cnt)
if N <= 20:
    hanoi_2(N, 1, 3, 2)
