from functools import cmp_to_key


def compare(a, b):
    if a + b > b + a:
        return -1  # a+b가 크면 a 앞으로
    if a + b < b + a:
        return 1
    return 0


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    c = "".join(numbers)

    if c[0] == "0":
        return "0"
    return c


solution([3, 30, 34, 5, 9])
