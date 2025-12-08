"""
조합으로 풀면될듯
start 인덱스를 점점 늘려서

"""

import sys

found = False


def seven_dwarf_combi(arr, result, start, depth, sum_height=100):
    global found
    if found:
        return True
    if depth == len(result) and sum(result) == sum_height:
        found = True
        return True
    if depth == len(result):
        return False

    for i in range(start, len(arr)):
        if found:
            break
        result[depth] = arr[i]
        seven_dwarf_combi(arr, result, i + 1, depth + 1, sum_height)

    return True


dwarp_data = [int(sys.stdin.readline()) for i in range(9)]
result = [0] * 7

depth = 0
sum_height = 100

seven_dwarf_combi(dwarp_data, result, 0, depth, sum_height)

result.sort()
for item in result:
    print(item)
