def solution(answers):
    people1 = [1, 2, 3, 4, 5]
    people2 = [2, 1, 2, 3, 2, 4, 2, 5]
    people3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt = [0, 0, 0]

    # 나머지 연산 5, 8, 10
    for idx, ans in enumerate(answers):
        if people1[idx % 5] == ans:
            cnt[0] += 1
        if people2[idx % 8] == ans:
            cnt[1] += 1
        if people3[idx % 10] == ans:
            cnt[2] += 1

    winner = max(cnt)
    answer = []
    for idx, i in enumerate(cnt):
        if i == winner:
            answer.append(idx + 1)

    return answer
