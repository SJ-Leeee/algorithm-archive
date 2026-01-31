# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
# n을 돌리며 stack생성 스택에는 (가격, 들어온시간)
# 스택에 들어올때 만약 스택0이 나보다 크면 내보내버리기 0만 내보내면됨 while로


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


solution([1, 2, 3, 2, 3])
