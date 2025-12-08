# 스택에 넣으면 됨 그냥

# [ or ( 시에는 pop
# ] or ) 시에는 Push

# 스택에 넣을때는 곱해야 할 상수를 두셈
# 꺼낼때는 그것을 제외하셈


a = "(()[[]])([])"
a = list(a)
stack = []
result = 1
# 연속이면 누적값들을 곱하기

flag = False
cum_value = 0
for item in a:
    if item == "(":
        stack.append(item)
        flag = False
    if item == "[":
        stack.append(item)
        flag = False

    if item == ")":
        removed = stack.pop() # 하나뽑고
        if removed != "(":
            result = 0
            break

        if flag:
            cum_value *= 2
        else:
            cum_value += 2
            flag = True


print(result)

# 카운트가 맞으면 스택앞에 거 곱해서 나가라


# for i in range(len(a) - 1, -1, -1):
#     if a[i] == "]":
#         stack.append(a[i])
#         count_num_3 += 1
#         stack_product *= 3
#     elif a[i] == ")":
#         stack.append(a[i])
#         count_num_2 += 1
#         stack_product *= 2
#     elif a[i] == "(":
#         removed = stack.pop()
#         count_num_2 -= 1
#         if removed != ")":
#             result = 0
#             break

#         if count_num_2 == 0:
#             result = result + (stack_product * 2)
#             stack_product //= 2

#         if len(stack) == 0:
#             continue
#         result = result + (stack_product * 2)
#     elif a[i] == "[":
#         removed = stack.pop()
#         if removed != "]":
#             result = 0
#             break
#         stack_product //= 3
#         if len(stack) == 0:
#             continue
#         result += stack_product * 3


# num3_stack_count = 0
# num2_stack_count = 0

# num3_cum_count = 0
# num2_cum_count = 0

# stack_cum = 1
# for i in range(len(a) - 1, -1, -1):
#     if a[i] == "]":
#         stack.append(a[i])
#         num3_stack_count += 1  # 스택의 3의 개수
#         stack_cum *= 3  # 스택 안의 곱
#     if a[i] == ")":
#         stack.append(a[i])
#         num2_stack_count += 1  # 스택의 2의 개수
#         stack_cum *= 2  # 스택 안의 곱

#     if a[i] == "(":
#         removed = stack.pop()
#         # 자기랑 누적했던거랑 스택에 남은거
#         if removed != ")":
#             result = 0
#             break
#         num2_stack_count -= 1  # 스택카운트 감소
#         stack_cum //= 2  # 스택 안의 곱

#         if num2_stack_count > 0:
#             num2_cum_count += 1
#         elif num2_stack_count == 0:
#             result = result * 2 * (2**num2_cum_count) * stack_cum  # 리절트에 더하고
#             num2_cum_count = 0

#     if a[i] == "[":
#         removed = stack.pop()
#         # 자기랑 누적했던거랑 스택에 남은거
#         if removed != "]":
#             result = 0
#             break
#         num3_stack_count -= 1  # 스택카운트 감소
#         stack_cum //= 3  # 스택 안의 곱

#         if num3_stack_count > 0:
#             num3_cum_count += 1
#         elif num3_stack_count == 0:
#             result = result * 3 * (3**num3_cum_count) * stack_cum  # 리절트에 더하고
#             num3_cum_count = 0
