def solution(nums):
    diff = 0
    half = len(nums) // 2
    pocketmon_dict = {}

    for i in nums:
        if i not in pocketmon_dict:
            pocketmon_dict[i] = True
            diff += 1

    return half if diff >= half else diff
