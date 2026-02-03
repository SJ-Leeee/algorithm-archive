import sys


N = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split()))
budget_sum = int(sys.stdin.readline())


def solutions(budgets, budget_sum):
    if sum(budgets) <= budget_sum:
        return max(budgets)

    budgets.sort()
    left, right = budget_sum // N - 1, budgets[-1]  # 상한가 최소는 N으로 나눈것과 같다

    while left < right:
        mid = (left + right) // 2

        cut_budget = 0
        for b in budgets:
            if b > mid:
                cut_budget += mid
            else:
                cut_budget += b

        # 만약 정리된게 요구보다 많으면 상한액을 더 낮춰야함
        # 만약 정리된게 요구보다 같거나 적으면 상한액을 더 올려야함 (최대값)
        if cut_budget <= budget_sum:
            left = mid + 1
        else:
            right = mid

    return left - 1


print(solutions(budgets, budget_sum))