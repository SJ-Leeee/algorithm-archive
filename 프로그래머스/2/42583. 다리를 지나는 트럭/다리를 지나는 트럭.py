
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
    
    return last_sec + 1