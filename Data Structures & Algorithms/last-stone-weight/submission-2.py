# import heapq
# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
        
#         maxHeap = [-i for i in stones]
#         heapq.heapify(maxHeap)

#         while len(maxHeap) >= 2:
#             y = -heapq.heappop(maxHeap)
#         #     x = -heapq.heappop(maxHeap)

#         #     if x < y:
#         #         heapq.heappush(maxHeap, -(y-x))
#         #     elif x == y:
#         #         continue

#         # return -maxHeap[0] if maxHeap else 0






import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = [-i for i in stones]
        heapq.heapify(max_heap)

        while len(max_heap) >= 2:

            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)

            if x < y:
                heapq.heappush(max_heap, -(y-x))
            elif x == y:
                continue

        return -max_heap[0] if max_heap else 0















     