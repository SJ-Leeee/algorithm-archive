def find_hansu(num, count):
    if num < 100:
        return num

    hundreds_digit = num // 100
    count += 99
    count += (hundreds_digit - 1) * 5

    i = 0
    while hundreds_digit + (2 * i) < 10:
        hansu = (
            hundreds_digit * 100 + (hundreds_digit + i) * 10 + hundreds_digit + (2 * i)
        )
        if num >= hansu:
            count += 1
        i += 1

    j = -1
    while hundreds_digit + (2 * j) >= 0:
        hansu = (
            hundreds_digit * 100 + (hundreds_digit + j) * 10 + hundreds_digit + (2 * j)
        )
        if num >= hansu:
            count += 1
        j -= 1

    return count


N = int(input())
a = find_hansu(N, 0)
print(a)
