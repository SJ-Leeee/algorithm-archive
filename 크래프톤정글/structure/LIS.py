"""
첫번째 방법 dp

O(n**2)
"""


def lis_dp():
    data = [1, 5, 4, 2, 3, 8, 6, 7, 9, 3, 4, 5]

    length = len(data)
    dp = [1] * length

    for i in range(1, length):
        for j in range(i):
            if data[i] > data[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))


# lis_dp()

"""
이분탐색을 이용하는 방법
"""


def lis_bintree():
    data = [1, 5, 4, 2, 3, 8, 6, 7, 9, 3, 4, 5]
    result = []
    result.append(data[0])
    for i in range(1, len(data)):
        if data[i] > result[-1]:
            result.append(data[i])
        else:
            left = lower_bound(result, data[i])
            result[left] = data[i]
        print(result)
    # 이하의 최대값


def lower_bound(arr, target):
    """target 이상인 첫 위치"""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:  # 🎯 < 사용
            left = mid + 1
        else:
            right = mid
    return left


lis_bintree()
