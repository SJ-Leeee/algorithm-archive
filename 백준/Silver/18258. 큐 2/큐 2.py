from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
queue = deque()
result = []

for _ in range(N):
    line = input().split()
    cmd = line[0]

    match cmd:
        case "push":
            queue.append(int(line[1]))
        case "pop":
            result.append(queue.popleft() if queue else -1)
        case "size":
            result.append(len(queue))
        case "empty":
            result.append(0 if queue else 1)
        case "front":
            result.append(queue[0] if queue else -1)
        case "back":
            result.append(queue[-1] if queue else -1)

print("\n".join(map(str, result)))