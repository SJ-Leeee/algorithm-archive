# """
# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여섯 가지이다.

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# """

# """
# 15
# push 1
# push 2
# front
# back
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# front
# """

# from collections import deque
# import sys


# def command_factory(cmd, num=None):
#     if cmd == "push":
#         queue.append(num)

#     elif cmd == "pop":
#         if not queue:
#             result.append(-1)
#         else:
#             result.append(queue.popleft())

#     elif cmd == "size":
#         result.append(len(queue))

#     elif cmd == "empty":
#         if queue:
#             result.append(0)
#         else:
#             result.append(1)
#     elif cmd == "front":
#         if queue:
#             result.append(queue[0])
#         else:
#             result.append(-1)
#     elif cmd == "back":
#         if queue:
#             result.append(queue[-1])
#         else:
#             result.append(-1)


# N = int(sys.stdin.readline())
# queue = deque()
# result = []

# for _ in range(N):
#     cmd = sys.stdin.readline().split()

#     if len(cmd) > 1:
#         command_factory(cmd[0], int(cmd[1]))
#     else:
#         command_factory(cmd[0])


# for i in result:
#     print(i)


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
