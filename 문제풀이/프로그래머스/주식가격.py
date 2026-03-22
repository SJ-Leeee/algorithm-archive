"""
스택을 사용해서 나보나 높으면 없애버려.

"""


def solution(prices):

    answer = [-1] * len(prices)
    stack = []
    for idx, i in enumerate(prices):
        while stack and stack[-1][0] > i:  # 뺄거 다빼고
            _, exit_idx = stack.pop()
            answer[exit_idx] = idx - exit_idx

        stack.append((i, idx))  # 넣기

    full_time = len(prices) - 1
    while stack:
        _, exit_idx = stack.pop()
        answer[exit_idx] = full_time - exit_idx

    return answer
