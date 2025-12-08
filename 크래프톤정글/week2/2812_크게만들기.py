"""
1. count가 남아있을 시 스택에서 모두 제거
2. 모두 들어갔는데 도 count가 남아있으면 스택에서 Pop
"""

import sys


stack = []


N, cnt = map(int, sys.stdin.readline().split())

a = sys.stdin.readline().strip()

lis_a = list(a)

for i in lis_a:
    if len(stack) == 0 or cnt == 0:
        stack.append(i)
    else:
        while len(stack) > 0:
            if int(stack[-1]) < int(i) and cnt > 0:
                stack.pop()
                cnt -= 1
            else:
                break
        stack.append(i)

while cnt > 0:
    stack.pop()
    cnt -= 1


print("".join(stack))
