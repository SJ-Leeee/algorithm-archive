import bisect
from itertools import combinations


def solution(info, query):
    people_dict = {}

    for i in info:
        lang, pos, duty, food, score = i.split()
        score = int(score)
        key = f"{lang[0]}-{pos[0]}-{duty[0]}-{food[0]}"

        # 원본 키 + 모든 - 조합 키 생성
        keys = [key]
        for co in range(1, 5):
            for c in combinations([0, 2, 4, 6], co):
                tmp = list(key)
                for d in c:
                    tmp[d] = "-"
                keys.append("".join(tmp))

        for k in keys:
            if k not in people_dict:
                people_dict[k] = []
            people_dict[k].append(score)

    # 미리 정렬
    for k in people_dict:
        people_dict[k].sort()

    answer = []
    for que in query:
        que = que.split()
        find_key = f"{que[0][0]}-{que[2][0]}-{que[4][0]}-{que[6][0]}"
        score = int(que[7])

        if find_key in people_dict:
            values = people_dict[find_key]
            idx = bisect.bisect_left(values, score)
            answer.append(len(values) - idx)
        else:
            answer.append(0)

    return answer