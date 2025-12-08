def permutation_swap(arr, start, r):
    if start == r:
        print(arr[:r])
        return

    for i in range(start, len(arr)):
        arr[start], arr[i] = arr[i], arr[start]
        permutation_swap(arr, start + 1, r)
        arr[i], arr[start] = arr[start], arr[i]


permutation_swap([1, 2, 3, 4], 0, 3)

# 스왑방식은 순서가 보장되지 않음
