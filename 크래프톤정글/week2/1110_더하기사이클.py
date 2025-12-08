# 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.

import sys


N = int(sys.stdin.readline())


if N < 10:
    N *= 10
origin_N = N
count = 1

while True:
    tens_digit = N // 10
    ones_digit = N % 10

    temp = tens_digit + ones_digit
    temp_one = temp % 10

    N = ones_digit * 10 + temp_one

    if N == origin_N:
        break

    count += 1

print(count)
