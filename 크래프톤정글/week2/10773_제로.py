# push pop만 존재하면된다

import sys


record = []
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        record.append(num)
    else:
        record.pop()

print(sum(record))
