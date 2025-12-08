import random
import sys
import time


def merge_sort(num_list):
    length = len(num_list)
    if length < 2:
        return num_list
    # 좌측과 우측을 나눠서 보낸다
    half = len(num_list) // 2
    left_list = num_list[:half]
    right_list = num_list[half:]
    left = merge_sort(left_list)
    right = merge_sort(right_list)

    return merge_helper(left, right)


def merge_helper(left_list, right_list):
    i = 0
    j = 0

    temp = []

    while len(left_list) > i and len(right_list) > j:
        if left_list[i] >= right_list[j]:
            temp.append(right_list[j])
            j += 1
        else:
            temp.append(left_list[i])
            i += 1

    while len(left_list) > i:
        temp.append(left_list[i])
        i += 1

    while len(right_list) > j:
        temp.append(right_list[j])
        j += 1

    return temp


N = int(sys.stdin.readline())
# random_list = [random.randint(1, 200000) for _ in range(1000000)]
start = time.time()
data = [int(sys.stdin.readline()) for i in range(N)]
a = merge_sort(data)
for i in a:
    print(i)
end = time.time()
print(f"{end - start:.5f} sec")
