from collections import deque


def solution(priorities, location):
    deq = deque()  # 메인 큐
    priority_deq = deque(priorities)  # max 비교 큐
    rank = 1
    for idx, proper in enumerate(priorities):
        deq.append((proper, idx))

    while deq:  # 메인 다 사라질때까지
        entity = deq.popleft()  # (proper, idx)
        priority_deq.popleft()  # max용 큐

        max_proper = max(priority_deq) if priority_deq else 0

        if entity[0] < max_proper:  # 작으면 다시 넣고
            deq.append(entity)
            priority_deq.append(entity[0])
        else:
            if location == entity[1]:
                return rank
            rank += 1



