from heapq import *
#push, pop 할때마다 자동 정렬

def solution(scoville, K):
    count = 0
    heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        num1 = heappop(scoville)
        num2 = heappop(scoville)
        heappush(scoville, num1 + num2 * 2)
        count += 1
    return count if scoville[0] >= K else -1 #모든 음식의 스코빌 지수를 K이상으로 만들 수 없는 경우 -1을 return