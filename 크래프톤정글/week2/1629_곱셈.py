import time


# memory = {}


# def multiplication(num, expo, c):
#     if expo == 1:
#         return num

#     if expo in memory:
#         return memory[expo]
#     else:
#         half = expo // 2
#         memory[expo] = multiplication(num, half) * multiplication(num, expo - half)
#         return memory[expo]


# def test(num, expo):
#     if expo == 1:
#         return num
#     half = expo // 2

#     return test(num, half) * test(num, expo - half)


# start1 = time.time()
# a = multiplication(10, 50)
# print(a)
# end1 = time.time()
# start2 = time.time()
# b = test(10, 50)
# print(b)
# end2 = time.time()
# print(f"{end1 - start1:.5f} sec")
# print(f"{end2 - start2:.5f} sec")

# 10 11 12
# 나머지에는 패턴이 있다.


# def gobsem(num, opp, m_num):
#     memory = []
#     seen = {}
#     for i in range(1, opp + 1):  # 1부터 opp번까지 순회
#         if i - 1 in seen:
#             result = seen[i - 1] * num
#             seen[i] = result
#         else:
#             result = num**i
#             seen[i] = result

#         mod = result % m_num

#         if len(memory) >= 2 and memory[1] == mod:
#             break
#         memory.append(mod)

#     circle = memory[1:]
#     circle_len = len(circle)
#     find_idx = (opp - 1) % circle_len - 1
#     print(circle[find_idx])


# a, b, c = map(int, input().split())
# gobsem(a, b, c)
# start1 = time.time()
# end1 = time.time()
# print(f"{end1 - start1:.5f} sec")

# memory = []
#     count = 0
#     for i in range(1, opp + 1):  # 1부터 opp번까지 순회
#         count += 1
#         mod = num**i % m_num
#         if len(memory) >= 2 and memory[1] == mod:
#             break
#         memory.append(mod)

#     circle = memory[1:]
#     circle_len = len(circle)
#     find_idx = (opp - 1) % circle_len - 1
#     print(circle[find_idx])


def mod_number_recursion(number, exponent, m_number):
    # 지수가 1이라면 리턴
    if exponent == 1:
        return number % m_number

    # 지수의 절반 재귀
    k = mod_number_recursion(number, exponent // 2, m_number)
    if exponent % 2 == 0:
        # 짝수일 경우 제곱만 해서 리턴
        return (k * k) % m_number
    else:
        # 홀수일 경우 제곱에 number를 곱해서 리턴
        return (k * k * number) % m_number


a, b, c = map(int, input().split())
mod_number_recursion(a, b, c)
