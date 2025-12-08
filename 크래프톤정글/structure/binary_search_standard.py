# 🎯 이분탐색 패턴 완전정리 - 외우기용!


def binary_search_template(arr, target, condition_type):
    """
    모든 이분탐색을 하나의 템플릿으로!

    조건 타입:
    - 'first_gte': target 이상인 첫 위치 (Lower Bound)
    - 'first_gt': target 초과인 첫 위치 (Upper Bound)
    - 'last_lt': target 미만인 마지막 위치
    - 'last_lte': target 이하인 마지막 위치
    """
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if condition_type == "first_gte":
            # target 이상인 첫 위치
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid

        elif condition_type == "first_gt":
            # target 초과인 첫 위치
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid

        elif condition_type == "last_lt":
            # target 미만인 마지막 위치 (뒤에서부터)
            if arr[len(arr) - 1 - mid] >= target:
                left = mid + 1
            else:
                right = mid

        elif condition_type == "last_lte":
            # target 이하인 마지막 위치 (뒤에서부터)
            if arr[len(arr) - 1 - mid] > target:
                left = mid + 1
            else:
                right = mid

    return left


# 🔥 실전에서 자주 쓰는 4가지 패턴만 외우세요!


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


def upper_bound(arr, target):
    """target 초과인 첫 위치"""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:  # 🎯 <= 사용 (여기만 다름!)
            left = mid + 1
        else:
            right = mid
    return left


def find_exact(arr, target):
    """정확한 값 찾기"""
    pos = lower_bound(arr, target)
    if pos < len(arr) and arr[pos] == target:
        return pos
    return -1


def parametric_search(check_function, min_val, max_val):
    """매개변수 탐색 (조건을 만족하는 최소/최대값)"""
    left, right = min_val, max_val + 1
    while left < right:
        mid = (left + right) // 2
        if check_function(mid):  # 조건 만족하면
            right = mid  # 더 작은 값 시도
        else:
            left = mid + 1  # 더 큰 값 필요
    return left


# 🎪 암기용 치트시트
"""
🔥 무조건 외울 것:

1. 시작: left=0, right=len(arr)
2. 반복: while left < right
3. 중점: mid = (left + right) // 2  
4. 업데이트: 
   - left = mid + 1  (mid는 답이 아님)
   - right = mid     (mid는 답 후보)

5. 조건 패턴:
   - Lower Bound: if arr[mid] < target
   - Upper Bound: if arr[mid] <= target  (=만 추가!)
   
6. 결과: left가 답
"""

# 🧪 테스트 및 검증
if __name__ == "__main__":
    arr = [1, 2, 4, 4, 4, 6, 7, 9]
    target = 4

    print(f"배열: {arr}")
    print(f"타겟: {target}")
    print(f"Lower bound (4 이상 첫 위치): {lower_bound(arr, target)}")  # 2
    print(f"Upper bound (4 초과 첫 위치): {upper_bound(arr, target)}")  # 5
    print(f"정확한 위치: {find_exact(arr, target)}")  # 2
    print(f"4의 개수: {upper_bound(arr, target) - lower_bound(arr, target)}")  # 3

    # 없는 값 테스트
    print(f"\n없는 값 5 테스트:")
    print(f"Lower bound: {lower_bound(arr, 10)}")  # 5 (6의 위치)
    print(f"Upper bound: {upper_bound(arr, 10)}")  # 5 (6의 위치)
    print(f"정확한 위치: {find_exact(arr, 10)}")  # -1
