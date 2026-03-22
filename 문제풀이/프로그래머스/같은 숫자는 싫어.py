"""
1. 배열은 0~9까지의 숫자로 이루어져 있다.
2. 연속적으로 나타나는 숫자는 하나만 남기고 제거
3. 원소들의 숫자 순서는 유지해야 한다.

--- 구현
1. arr를 순회
2. 순회한 원소들을 stack(가장최근)에 넣고 top과 비교.
3. stack을 반환
"""


def solution(arr):
    stack = []
    for i in arr:
        if not stack or stack[-1] != i:
            stack.append(i)

    return stack


solution([1, 1, 3, 3, 0, 1, 1])
# 5분
