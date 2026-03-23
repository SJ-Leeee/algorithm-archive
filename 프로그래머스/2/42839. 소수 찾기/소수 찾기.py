from itertools import permutations
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  # 소수 아님
    return True  # 소수


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    for i in set(numbers):
        if is_prime(int(i)):
            answer += 1

    for i in range(2, len(numbers) + 1):
        perm = list(set(permutations(numbers, i)))
        for j in perm:
            if j[0] == "0":
                continue
            if is_prime(int("".join(j))):
                answer += 1

    return answer
