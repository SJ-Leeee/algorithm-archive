def solution(prices):
    answer = [-1] * len(prices)
    stack = []
    for idx, val in enumerate(prices):

        # 스택이 비었으면 그냥 삽입
        if len(stack) == 0:
            stack.append((val, idx))
            continue
        # 스택이 존재하고 현재값이 마지막값보다 크다면 삽입
        if len(stack) > 0 and val >= stack[-1][0]:
            stack.append((val, idx))
            continue

        # 여기는 스택값이 존재하고 마지막값이 현재값보다 작음
        while 1:
            if len(stack) == 0 or (len(stack) > 0 and val >= stack[-1][0]):
                stack.append((val, idx))
                break
            _, s_idx = stack.pop()
            answer[s_idx] = idx - s_idx

    while len(stack) > 0:
        _, idx = stack.pop()
        answer[idx] = len(prices) - idx - 1

    return answer