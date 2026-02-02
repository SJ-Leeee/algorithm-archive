import sys


while True:
    line = sys.stdin.readline()
    if line == ".\n":
        break
    line = line.strip()
    
    stack = []
    result = "yes"
    for c in line:
        if c == "[" or c == "(":
            stack.append(c)

        if c == "]":
            if not stack or stack.pop() != "[":
                result = "no"
                break
        if c == ")":
            if not stack or stack.pop() != "(":
                result = "no"
                break
    if stack:
        result = "no"
    print(result)
    # print(line)
