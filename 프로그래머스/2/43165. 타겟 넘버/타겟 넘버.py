def dfs(numbers, depth, target, summ):
    if depth == len(numbers):
        if target == summ:
            return 1
        return 0
    
    a = dfs(numbers, depth + 1, target, summ + numbers[depth])
    b = dfs(numbers, depth + 1, target, summ - numbers[depth])
    return a + b
    
def solution(numbers, target):
    return dfs(numbers, 0, target, 0)
        
# [1, 1, 1, 1, 1]	3	5
# 방법의 수를 아는것이므로 dfs도 괜찮음.