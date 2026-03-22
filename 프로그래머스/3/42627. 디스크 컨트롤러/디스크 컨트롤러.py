from collections import deque
import heapq


def insert_wait_queue(sec, wait_queue, jobs_deq):
    if not jobs_deq:
        return

    while jobs_deq and jobs_deq[0][1] <= sec:
        cost, req_time, idx = jobs_deq.popleft()
        heapq.heappush(wait_queue, (cost, req_time, idx))


def solution(jobs):

    n_jobs = []
    for idx, i in enumerate(jobs):
        n_jobs.append((i[1], i[0], idx))  # 소요시간 요청시간 인덱스
    n_jobs.sort(key=lambda x: x[1])  # 들어온시간으로 오름차순
    jobs_deq = deque(n_jobs)  # 큐 형태로 전환
    sec = 0  # 현재시간
    total_time = 0
    wait_queue = []

    insert_wait_queue(sec, wait_queue, jobs_deq)  # 삽입

    # job이 없어질때까지
    while jobs_deq:
        # wait_queue가 있다면 계속순환
        while wait_queue:
            cost, req_time, ss = heapq.heappop(wait_queue)

            sec = sec + cost
            total_time += sec - req_time
            insert_wait_queue(sec, wait_queue, jobs_deq)

        # 이경우엔 deq가 없던가 아님 남아있는데 아직 안온거임
        sec += 1
        insert_wait_queue(sec, wait_queue, jobs_deq)

    while wait_queue:
        cost, req_time, _ = heapq.heappop(wait_queue)
        sec = sec + cost
        total_time += sec - req_time

    return total_time // len(jobs)