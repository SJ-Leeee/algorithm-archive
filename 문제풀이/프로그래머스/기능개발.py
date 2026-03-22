"""
1. 작업 진행도가 우선순위 따라 들어온다.
2. 일별 진행속도가 speeds 배열에 들어온다.
3. a작업 처리후 되는것을 모두 제거한다.

---- 구현. deque를 이용해서 큐 형태로 처리해야함.
1. day를 1로 두고 시작
2. 100 - a = 7  // speed = 7 = day가 되는것
3. 다음것. 100- a = remain = 70 . 만약에 day * speed 가
remain넘으면pop 아니면 day를 다시 선정 어떻게? remain // speed
"""

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


solution([93, 30, 55], [1, 30, 5])
"""

from collections import deque


def solution(progresses, speeds):
    # 프로그래스가 다 빠질때까지
    ## 다음프로그래스가 day*speed가 넘어갈때까지
    result = []
    pr_deq = deque(progresses)
    spd_deq = deque(speeds)
    day = 0
    while pr_deq:
        add_cnt = 0
        # 만약에 안통과면?
        remain = 100 - pr_deq[0]
        day = remain // spd_deq[0]
        add_cnt += 1
        pr_deq.popleft()
        spd_deq.popleft()

        # 만약에 넘기면 add_cnt추가야. 여긴 통과
        while pr_deq and 100 - pr_deq[0] <= spd_deq[0] * day:
            pr_deq.popleft()
            spd_deq.popleft()
            add_cnt += 1

    return result


"""
