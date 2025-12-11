
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
