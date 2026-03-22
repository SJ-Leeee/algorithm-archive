"""
1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
  3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
"""

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


solution([1, 1, 9, 1, 1, 1], 0)

# max도 빈값이면 오류난다.
# 23분

"""
# 리스트 컴프리헨션 - 리스트 만듦
[x[0] for x in deq]

# 제너레이터 표현식 - 리스트 안 만듦
(x[0] for x in deq)

# max에 바로 넣을 때
max(x[0] for x in deq)
"""
