import heapq


class DualPriorityQueue:
    def __init__(self):
        self.min_heap = []  # 최솟값용
        self.max_heap = []  # 최댓값용 (음수로)
        self.deleted = {}  # 삭제 표시

    def push(self, val):
        heapq.heappush(self.min_heap, val)
        heapq.heappush(self.max_heap, -val)

    def pop_min(self):
        while self.min_heap:
            val = heapq.heappop(self.min_heap)
            # 만약 삭제처리된것이였으면 pass
            if self.deleted.get(val, 0) > 0:
                self.deleted[val] -= 1
                continue

            self.deleted[val] = self.deleted.get(val, 0)
            self.deleted[-val] = self.deleted.get(-val, 0) + 1
            # 최대힙에 삭제 표시
            return val
        return 0

    def pop_max(self):
        while self.max_heap:
            val = -heapq.heappop(self.max_heap)
            # 만약 삭제처리된것이였으면 pass
            if self.deleted.get(-val, 0) > 0:
                self.deleted[-val] -= 1
                continue

            # 최소힙에 삭제 표시
            self.deleted[val] = self.deleted.get(val, 0) + 1
            self.deleted[-val] = self.deleted.get(-val, 0)
            return val
        return 0


def solution(operations):
    dual_queue = DualPriorityQueue()
    for i in operations:
        cmd, num = i.split()
        num = int(num)
        if cmd == "I":
            dual_queue.push(num)
        else:
            if num == 1:
                dual_queue.pop_max()
            else:
                dual_queue.pop_min()

    return [dual_queue.pop_max(), dual_queue.pop_min()]


oper = ["I 3", "I 3", "D 1", "D 1"]
print(solution(oper))
