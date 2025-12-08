import sys

# 25 10 5 1
N = int(sys.stdin.readline())
five_cnt = 0

min_count = -1

if N % 5 == 0:
    print(N // 5)
else:
    while N > 0:
        if N % 3 == 0:  # 3의 배수면
            min_count = N // 3 + five_cnt
        N -= 5
        five_cnt += 1

    print(min_count)
