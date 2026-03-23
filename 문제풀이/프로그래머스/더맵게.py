# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 최소 힙
import heapq


def solution(scoville, K):
    chance = 0
    heapq.heapify(scoville)  # 최소힙으로 변환

    while len(scoville) > 1 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        chance += 1

    if scoville[0] < K:
        return -1

    return chance
