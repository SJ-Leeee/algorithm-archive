def solution(clothes):
    answer = 1
    kind_dict = {}
    for _, kind in clothes:
        if kind in kind_dict:
            kind_dict[kind] += 1
        else:
            kind_dict[kind] = 2 # 안입는것까지 감안
    for i in kind_dict.values():
        answer *= i
    
    return answer - 1 
    
        