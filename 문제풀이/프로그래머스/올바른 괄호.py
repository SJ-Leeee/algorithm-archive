# 괄호는 ())() 이런식으로 들어온다.
# 스택문제
# ((()))


def solution(s):

    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if not stack:  # 스택 자체가 없으면
                return False
            stack.pop()

    if stack:
        return False

    return True


# 6분
