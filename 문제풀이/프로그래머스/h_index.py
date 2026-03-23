"""
어떤 과학자가 발표한 논문 n편 중,
h번 이상 인용된 논문이 h편 이상이고
나머지 논문이 h번 이하 인용되었다면
h의 최댓값이 이 과학자의 H-Index입니다.
"""

"""
이분 탐색 안해도 됨
최대 길이 1000.
1000~1까지 
"""


def solution(citations):
    max_h = len(citations)
    citations.sort(reverse=True)  # 내림차순 정렬
    h_idx = 0
    for i in range(max_h, 0, -1):  # h_idx. 즉 인용횟수
        cnt = 0
        for j in range(max_h):
            # 순회하면서 i보다 같거나 높으면 리턴. 이게 max
            if i > citations[j]:
                break
            cnt += 1
        if cnt >= i:
            h_idx = i
            break

    return h_idx


solution([2, 2, 1, 5, 1, 5, 5, 5, 5, 5])
