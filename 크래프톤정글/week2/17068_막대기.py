# 뒤에서부터 pop하며 높으면 체크, height 재설정

import sys


N = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline()) for _ in range(N)]
count = 1
print(arr)
height = arr[-1]
while len(arr) > 0:
    remove_item = arr.pop()
    if remove_item > height:
        count += 1
        height = remove_item

print(count)
