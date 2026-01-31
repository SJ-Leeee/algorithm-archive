"""
오름차순이면 안됨.. 다만 기준이있음
1 2 3 가능

4 1 2 3 불가능

첫숫자가 10이었어
그다음은 무조건 내림차순이어야돼. 오름차순이 있는순간 끝

10 2 4 불가능
10 4 2 가능

4 3 6 8 7 5 1 2 << 탈락
가장 큰 값을 기억해야하나?

max = 4
3 가능
max = 6
4 3 6 가능
max = 8
4 3 6 8 가능

오름차순인데 max보다 크면 괜찮음
"""

import sys

sys.stdin = open("input.txt", "r")  # 로컬 테스트 시 주석 해제
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]


def solution(arr):
    stack = []
    answer = []
    counter = 1
    for item in arr:
        while item >= counter:
            stack.append(counter)
            counter += 1
            answer.append("+")

        if stack and stack[-1] == item:
            stack.pop()
            answer.append("-")
        else:
            return "NO"

    return answer


answer = solution(arr)
if answer == "NO":
    print(answer)
else:
    for i in answer:
        print(i)
