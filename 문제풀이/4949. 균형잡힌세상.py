# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
# .

import sys


while True:
    line = sys.stdin.readline().strip()
    if not line:  # 빈 문자열이면 EOF
        break

    if line[-1] != ".":  # . 으로 끝나지않으면 탈락
        print("no")
        continue
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
    print(result)
    # print(line)
