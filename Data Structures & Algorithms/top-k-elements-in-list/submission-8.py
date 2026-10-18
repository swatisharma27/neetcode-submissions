import heapq
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        result = []

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1


        for num, count in freq.items():
            heapq.heappush(heap, (count, -num))

            if len(heap) > k:
                heapq.heappop(heap)

        for i in heap:
            result.append(-i[1])

        return result



        