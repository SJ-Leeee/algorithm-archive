
import heapq
def solution(operations):
    heap = []
    
    for op in operations:
        cmd, val = op.split()
        val = int(val)
        
        if cmd == "I":
            heapq.heappush(heap, val)
        else:
            if not heap:
                continue
            if val == 1:   # 최댓값 삭제
                heap.remove(max(heap))
                heapq.heapify(heap)
            else:          # 최솟값 삭제
                heapq.heappop(heap)
    
    if not heap:
        return [0, 0]
    return [max(heap), min(heap)]