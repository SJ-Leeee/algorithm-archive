import sys

# sys.stdin = open("input.txt", "r")  # 로컬 테스트 시 주석 해제
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
