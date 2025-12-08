import sys

N, money = map(int, sys.stdin.readline().split())

coins = []
for _ in range(N):
    c = int(sys.stdin.readline())
    coins.append(c)

coins.reverse()

result = 0
for coin in coins:
    if money == 0:
        break

    result += money // coin
    money %= coin

print(result)
