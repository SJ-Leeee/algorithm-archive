# 조합
# 리스트 받기.
# 리스트 순회하면서 set 하기
# 그 개수가 n/2 이게 최대횟수


def solution(nums):
    diff = 0
    half = len(nums) // 2
    pocketmon_dict = {}

    for i in nums:
        if i not in pocketmon_dict:
            pocketmon_dict[i] = True
            diff += 1

    return half if diff >= half else diff


a = solution([3, 3, 3, 2, 2, 4])

print(a)

# 11분
