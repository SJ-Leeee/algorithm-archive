from collections import deque
import sys


def command_factory(cmd, num=None):
    if cmd == "push":
        queue.append(num)

    elif cmd == "pop":
        if not queue:
            result.append(-1)
        else:
            result.append(queue.popleft())

    elif cmd == "size":
        result.append(len(queue))

    elif cmd == "empty":
        if queue:
            result.append(0)
        else:
            result.append(1)
    elif cmd == "front":
        if queue:
            result.append(queue[0])
        else:
            result.append(-1)
    elif cmd == "back":
        if queue:
            result.append(queue[-1])
        else:
            result.append(-1)


N = int(sys.stdin.readline())
queue = deque()
result = []

for _ in range(N):
    cmd = sys.stdin.readline().split()

    if len(cmd) > 1:
        command_factory(cmd[0], int(cmd[1]))
    else:
        command_factory(cmd[0])


for i in result:
    print(i)
