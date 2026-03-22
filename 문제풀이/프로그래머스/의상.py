def solution(clothes):
    type_dict = {}
    for item in clothes:
        c_type = item[1]  # 타입이름
        if c_type in type_dict:
            type_dict[c_type] += 1
        else:
            type_dict[c_type] = 1

    answer = 1
    for i in type_dict.values():

        answer *= i + 1

    return answer - 1


clothes = [
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
]

print(solution(clothes))
