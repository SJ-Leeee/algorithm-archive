"""
다리의 길이가 존재한다.
트럭마다 다리의길이를 추가시켜야한다.
단 트럭은 중첩될 수 있다.
트럭이 내려오는 시간도 알아야한다.

sec = 0 으로 시작한다.
트럭을 bridge_deq 에 넣는다. (weight, seq+bridge)
전체 중량을 추가한다. total += weight
만약 들어갈 수 없으면 브릿지 pop 한다. (while)
"""

from collections import deque


def solution(bridge_length, weight, truck_weights):
    sec = 0
    total_weight = 0
    bridge_deq = deque()

    for t in truck_weights:
        while t + total_weight > weight:  # 못올라감.
            exit_weight, exit_sec = bridge_deq.popleft()
            total_weight -= exit_weight
            sec = exit_sec if exit_sec > sec else sec

        # 올라갈수있는상태
        bridge_deq.append((t, sec + bridge_length))
        total_weight += t
        sec += 1

    _, last_sec = bridge_deq.pop()
    print(last_sec + 1)
    return last_sec + 1


solution(2, 10, [10, 10])
# 30분넘음
