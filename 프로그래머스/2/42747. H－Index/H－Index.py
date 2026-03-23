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