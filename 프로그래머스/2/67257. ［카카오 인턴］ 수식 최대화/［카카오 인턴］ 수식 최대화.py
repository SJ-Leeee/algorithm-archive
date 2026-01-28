from itertools import permutations

def solution(expression):
    # 연산자 → 함수 매핑 (if문 대신)
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b
    }
    
    def calc(expr, priority):
        # 우선순위 낮은 것부터 split (재귀 올라올 때 마지막에 계산됨)
        for op in priority:
            # 뒤에서부터 찾아야 왼쪽→오른쪽 계산 순서 유지
            idx = expr.rfind(op)
            if idx != -1:
                left = calc(expr[:idx], priority)
                right = calc(expr[idx+1:], priority)
                return ops[op](left, right)
        
        # 연산자 없으면 숫자
        return int(expr)
    
    answer = 0
    for perm in permutations(['+', '-', '*']):
        result = abs(calc(expression, perm))
        answer = max(answer, result)
    
    return answer