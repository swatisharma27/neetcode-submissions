import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)

            if x < y:
                heapq.heappush(maxHeap, -(y-x))
            elif x == y:
                continue

        return -maxHeap[0] if maxHeap else 0

     