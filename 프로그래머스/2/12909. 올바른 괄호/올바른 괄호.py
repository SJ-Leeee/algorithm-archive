def solution(s):

    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if not stack or stack.pop() != "(":  # 스택 자체가 없으면
                return False

    if stack:
        return False

    return True
