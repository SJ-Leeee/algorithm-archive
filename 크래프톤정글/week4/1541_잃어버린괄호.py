# 55-50+40
from collections import deque
import sys

# a = sys.stdin.readline().strip()

# nums = []
# n_char = []
# oper_char = []

# for i in range(len(a)):
#     if i == len(a) - 1:
#         n_char.append(a[i])
#         num = int("".join(n_char))
#         nums.append(num)
#     if a[i] == "-" or a[i] == "+":  # -였을때와 +였을때를 나눔
#         num = int("".join(n_char))
#         n_char.clear()
#         oper_char.append(a[i])
#         nums.append(num)
#     else:
#         n_char.append(a[i])

# oper_char.append("")
# sub_flag = False

# result = 0
# for i in range(len(nums)):
#     nums[i] = -nums[i] if sub_flag else nums[i]
#     result += nums[i]
#     if oper_char[i] == "-" and not sub_flag:
#         sub_flag = True

# print(result)


def v():
    a = sys.stdin.readline().strip()
    oper = []
    for char in a:
        if char == "+":
            oper.append(char)
        if char == "-":
            oper.append(char)
            break
    # [p,p,p,-] 요놈의 len부터 음수연산하면됨
    numbers = a.replace("+", ",").replace("-", ",").split(",")
    numbers = [int(x) for x in numbers if x]

    print(numbers)
    print(oper)
    sub_num = 0
    for i in range(len(oper), len(numbers)):
        sub_num -= numbers[i]

    print(numbers[0] + sub_num)


v()
