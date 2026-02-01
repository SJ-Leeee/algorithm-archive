import sys


N = int(sys.stdin.readline())


def hanoi_2(n, start, end, mid):
    if n == 1:
        print(start, end)
        return
    hanoi_2(n - 1, start, mid, end)
    print(start, end)
    hanoi_2(n - 1, mid, end, start)

print(2**N -1)
if N <= 20:
    hanoi_2(N, 1, 3, 2)
