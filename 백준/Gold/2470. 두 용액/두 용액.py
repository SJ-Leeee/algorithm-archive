import sys

N = int(sys.stdin.readline())
waters = list(map(int, sys.stdin.readline().split()))


best_couple = ()
best_diff = float('inf')
waters.sort()
left = 0
right = N - 1

while left < right:
    diff = waters[right] + waters[left]

    if diff == 0:
        best_couple = (waters[left], waters[right])
        break

    if best_diff > abs(diff):
        best_diff = abs(diff)
        best_couple = (waters[left], waters[right])

    if diff > 0:
        right -= 1
    else:
        left += 1

print(*best_couple)
