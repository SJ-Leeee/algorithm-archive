"""
1. 다리에 오를 수 있을때
    가장최근 시간에 +1 한 후 시간을 정하면됨
2. 다리에 오를 수 없을때
    가장앞에 있는 트럭을 내보내고, 시간은 그친구가 나간시간.
    이걸 들어갈수있을때까지 해야함.
"""

from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck = deque(truck_weights)
    bridge_truck = deque()
    bridge_sum = 0
    time = 0

    while truck:
        is_update = False
        while bridge_sum + truck[0] > weight or len(bridge_truck) + 1 > bridge_length:
            out_truck, out_time = bridge_truck.popleft()
            bridge_sum -= out_truck
            time = max(time, out_time + bridge_length)
            is_update = True

        time = time if is_update else time + 1

        t = truck.popleft()
        bridge_sum += t
        bridge_truck.append((t, time))

    _, ot = bridge_truck[-1]

    return ot + bridge_length


solution(3, 20, [7, 4, 10, 3, 16])


# while truck:

#     if bridge_sum + truck[0] <= weight and len(bridge_truck) + 1 <= bridge_length:
#         # 트럭이 올라갈수있을때
#         time += 1
#         t = truck.popleft()
#         bridge_sum += t
#         bridge_truck.append((t, time))
#     else:  # 못올라갈때
#         while (
#             bridge_sum + truck[0] > weight or len(bridge_truck) + 1 > bridge_length
#         ):
#             ot, otime = bridge_truck.popleft()  # 트럭을내보내고
#             bridge_sum -= ot  # 무게빼고
#             time = otime + bridge_length  # 최근시간을 갱신
#             t = truck.popleft()
#             bridge_sum += t  # 무게를 추가하고
#             bridge_truck.append((t, time))

#             if not truck:
#                 break

# print(bridge_truck)
# return bridge_truck[-1][1] + bridge_length  # 맨마지막트럭이 나가는것
