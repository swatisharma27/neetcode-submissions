import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        TC: O(n log k)
        SC: O(k)
        """
        
        heap = []
        result = []
    
        freq = {} # Euclidean : point

        x2, y2 = 0, 0

        for point in points:
            euclidean_dist = math.sqrt((point[0] - x2) ** 2 + (point[1] - y2) ** 2) 

            heapq.heappush(heap, (-euclidean_dist, point[0], point[1]))

            if len(heap) > k:
                heapq.heappop(heap)

        for dist, x, y in heap:
            result.append([x, y])

        return result