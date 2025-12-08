def get_prime_number(n):

    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, n // 2 + 1, 2):

        if (n % i) == 0:
            return False

    return True


def goldbah(num):
    half = num // 2

    for i in range(half, 0, -1):
        if get_prime_number(i) and get_prime_number(num - i):
            print(f"{i} {num - i}")
            return


N = int(input())

for _ in range(N):
     num = int(input())
     goldbah(num)