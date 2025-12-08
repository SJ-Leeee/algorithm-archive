"""
참고
https://st-lab.tistory.com/285
"""

# 동적 프로그래밍
# dp 를 설정하고 길이가 i가 1일때부터 최선의 선택


# dp = [1] * len(arr)

# for i in range(len(arr)):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j] + 1)

# print(dp)


# 길이만 구하는 과정 이분탐색


# else {
# 			// Lower Bound 이분탐색을 진행한다.
# 			int lo = 0;
# 			int hi = lengthOfLIS;
# 			while (lo < hi) {
# 				int mid = (lo + hi) / 2;

# 				if(LIS[mid] < key) {
# 					lo = mid + 1;
# 				}
# 				else {
# 					hi = mid;
# 				}


import sys

# {10, 20, 30, 15, 20, 30, 50, 40, 45 ,60}

lis = []

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

lis.append(arr[0])

for i in range(1, len(arr)):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
    else:
        right = len(lis)
        left = 0

        while left < right:
            mid = (right + left) // 2

            if lis[mid] < arr[i]:  # arr[i] 15가 크다면
                left = mid + 1
            else:
                right = mid
        lis[left] = arr[i]

print(len(lis))


# 자기보다 큰값만 찾으면 됨
# 없으면 추가
# 10, 20, 30, 15, 20, 30, 50, 40, 45 ,60
# for i in range(arr):

# def binary_serarch():
