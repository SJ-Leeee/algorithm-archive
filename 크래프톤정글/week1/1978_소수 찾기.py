n = int(input())
numbers = list(map(int, input().split()))
result = 0

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


for n in numbers:
    result += get_prime_number(n)
print(result)