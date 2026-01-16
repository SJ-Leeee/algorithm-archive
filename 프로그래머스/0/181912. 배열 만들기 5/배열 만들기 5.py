def solution(intStrs, k, s, l):
    answer = []
    for item in intStrs:
        ret = int(item[s:s+l])
        if ret > k:
            answer.append(ret)
    return answer