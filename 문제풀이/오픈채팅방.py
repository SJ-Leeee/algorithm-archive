test_case = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
]
# --- 여기서부터 문제 풀이 시작 ---


def solution(arr):
    result = []
    name_dict = {}
    for item in reversed(arr):
        part = item.split()
        if part[0] == "Enter" or part[0] == "Change":
            if part[1] not in name_dict:
                name_dict[part[1]] = part[2]

    for item in arr:
        act, uid, *rest = item.split()
        if act == "Enter":
            text = f"{name_dict[uid]}님이 들어왔습니다."
            result.append(text)
        elif act == "Leave":
            text = f"{name_dict[uid]}님이 나갔습니다."
            result.append(text)

    return result


print(solution(test_case))
