# [93, 30, 55]	[1, 30, 5]	[2, 1]


from collections import deque


def solution(progresses, speeds):
    answer = []
    remain_list = deque()
    for idx, item in enumerate(progresses):
        remain = 100 - item
        remainday = (remain + speeds[idx] - 1) // speeds[idx]
        remain_list.append(remainday)

    first_dep = -1
    deploy_cnt = 1
    while remain_list:
        if first_dep < remain_list[0]:
            first_dep = remain_list.popleft()
            answer.append(deploy_cnt)
            deploy_cnt = 1

        else:
            remain_list.popleft()
            deploy_cnt += 1
    answer.append(deploy_cnt)

    return answer[1:]


solution([93, 30, 55], [1, 30, 5])
