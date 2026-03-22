from collections import deque


def solution(progresses, speeds):
    # 프로그래스가 다 빠질때까지
    ## 다음프로그래스가 day*speed가 넘어갈때까지
    result = []
    pr_deq = deque(progresses)
    spd_deq = deque(speeds)
    day = 0
    while pr_deq:
        day += 1
        clear_cnt = 0
        # 만약 통과면
        while pr_deq and 100 - pr_deq[0] <= day * spd_deq[0]:
            clear_cnt += 1
            pr_deq.popleft()
            spd_deq.popleft()

        if clear_cnt > 0:
            result.append(clear_cnt)

    return result