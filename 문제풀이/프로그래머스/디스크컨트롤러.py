# 소요시간, 요청시간, 작업번호 의 우선순위로 최소힙
# 작업을 마친시간 기준으로 들어올 수 있는작업들을 최소힙에 삽입
# 다시 heapq pop
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
    while jobs_deq or wait_queue:
        # 대기큐 비어있으면 다음 작업 시작시간으로 점프
        if not wait_queue:
            sec = jobs_deq[0][1]  # 다음 작업 요청시간으로 바로 점프

        insert_wait_queue(sec, wait_queue, jobs_deq)

        cost, req_time, _ = heapq.heappop(wait_queue)
        sec += cost
        total_time += sec - req_time

        insert_wait_queue(sec, wait_queue, jobs_deq)

    return total_time // len(jobs)


jobs = [[0, 3], [1, 9], [3, 5]]
print(solution(jobs))


# 소요시간, 요청시간, 인덱스
# def solution(jobs):
#     jobs.sort(key=lambda x: x[0])  # 요청시각별로 정렬

#     sec = 0  # 현재시각
#     total_ret_time = 0
#     wait_queue = []  # 작업인덱스
#     job_deq = deque()

#     for idx, i in enumerate(jobs):
#         job_deq.append((i[1], i[0], idx))

#     while job_deq and job_deq[0][1] <= sec:
#         cost, req_time, j_idx = job_deq.popleft()
#         heapq.heappush(wait_queue, (cost, req_time, j_idx))

#     while job_deq:  # 작업이 있다면 계속 반복
#         while wait_queue:
#             cost, req_time, ab = heapq.heappop(wait_queue)
#             total_ret_time += (sec + cost) - req_time  # 반환시간 추가
#             # print(f"{sec}처리된것:({cost}, {req_time}, {ab}), total = {total_ret_time}")
#             sec = sec + cost  # 현재시간을 끝난시간으로 수정
#             # 처리하고 시간에 따라 추가한다. 이때 작업큐는 존재해야한다.
#             while job_deq and job_deq[0][1] <= sec:
#                 cost, req_time, j_idx = job_deq.popleft()
#                 # print(
#                 #     f"현재시간: {total_ret_time}, {wait_queue}, ({cost}, {req_time}, {j_idx})"
#                 # )
#                 heapq.heappush(wait_queue, (cost, req_time, j_idx))

#         # 여기까지 왔다는건 현재 시간이 부족하다는 뜻 혹은 작업이 이제 없거나
#         while job_deq and job_deq[0][1] <= sec:
#             cost, req_time, j_idx = job_deq.popleft()
#             heapq.heappush(wait_queue, (cost, req_time, j_idx))

#         sec += 1

#     while wait_queue:
#         cost, req_time, _ = heapq.heappop(wait_queue)
#         total_ret_time += (sec + cost) - req_time  # 반환시간 추가
#         # print(
#         #     f"{sec}마지막 처리된것:({cost}, {req_time}, {ab}), total = {total_ret_time}"
#         # )
#         sec = sec + cost  # 현재시간을 끝난시간으로 수정

#     return total_ret_time // len(jobs)


# jobs = [[0, 3], [1, 9], [3, 5]]
# print(solution(jobs))
