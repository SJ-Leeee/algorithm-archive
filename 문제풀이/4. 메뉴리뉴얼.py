"""
["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"][2, 3, 4]["AC", "ACDE", "BCFG", "CDE"]
"""

from itertools import combinations


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
courses = [2, 3, 4]

ret = ["AC", "ACDE", "BCFG", "CDE"]


def solution(orders, course):
    answer = []
    dictionary = {}
    for order in orders:
        o_list = list(order)  # 리스트로바꾸고
        max_cnt = len(o_list)
        o_list.sort()  # 알파벳순으로 변경

        for cnt in course:  # cnt개의 메뉴구성
            if max_cnt < cnt:
                break

            for comb in combinations(o_list, cnt):
                menu = "".join(comb)
                if menu in dictionary:
                    dictionary[menu] += 1
                else:
                    dictionary[menu] = 1
    # 길이별로 최댓값 뽑기
    for cnt in course:
        # 해당 길이인 것만 필터
        candidates = [
            (menu, count)
            for menu, count in dictionary.items()
            if len(menu) == cnt and count >= 2
        ]

        if not candidates:
            continue

        max_count = max(c for _, c in candidates)

        for menu, count in candidates:
            if count == max_count:
                answer.append(menu)
    answer.sort()

    return answer


solution(orders, courses)
