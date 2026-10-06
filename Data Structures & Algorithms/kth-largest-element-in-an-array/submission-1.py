import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        N = len(nums)
        for i in range(N):
            heapq.heappush(heap, nums[i])

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]