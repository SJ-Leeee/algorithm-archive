# # 비효율 제거버전
# def solution(prices):
#     n = len(prices)
#     answer = [0] * n # 1. 0으로 초기화 (가장 빠름)
#     stack = [] # 인덱스만 저장

#     for i, price in enumerate(prices):
#         # 2. 스택이 있고, 현재 가격이 스택의 top 가격보다 떨어졌다면 반복 (Pop)
#         while stack and prices[stack[-1]] > price:
#             j = stack.pop()
#             answer[j] = i - j # 떨어진 시점 - 과거 시점 = 유지 시간
        
#         # 3. 현재 시점은 아직 안 떨어졌으니 스택에 저장 (Push)
#         # 위 while문이 끝나면 스택은 항상 오름차순(유지 포함) 상태가 됨
#         stack.append(i) 

#     # 4. 끝까지 가격이 떨어지지 않고 스택에 남은 인덱스 처리
#     while stack:
#         j = stack.pop()
#         answer[j] = n - 1 - j

#     return answer

# def solution(prices):
#     answer = [-1] * len(prices)
#     stack = []
#     for idx, val in enumerate(prices):

#         # 스택이 비었으면 그냥 삽입
#         if len(stack) == 0:
#             stack.append((val, idx))
#             continue
#         # 스택이 존재하고 현재값이 마지막값보다 크다면 삽입
#         if len(stack) > 0 and val >= stack[-1][0]:
#             stack.append((val, idx))
#             continue

#         # 여기는 스택값이 존재하고 마지막값이 현재값보다 작음
#         while 1:
#             if len(stack) == 0 or (len(stack) > 0 and val >= stack[-1][0]):
#                 stack.append((val, idx))
#                 break
#             _, s_idx = stack.pop()
#             answer[s_idx] = idx - s_idx

#     while len(stack) > 0:
#         _, idx = stack.pop()
#         answer[idx] = len(prices) - idx - 1

#     return answer

def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for idx, price in enumerate(prices):

        while stack and stack[-1][0] > price:
            _, time = stack.pop()
            answer[time] = idx - time

        stack.append((price, idx))

    
    while stack:
        _, time = stack.pop()
        answer[time] = len(prices) - 1 - time

    return answer