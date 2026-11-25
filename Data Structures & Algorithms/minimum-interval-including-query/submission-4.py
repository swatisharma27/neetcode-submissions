import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        intervals = [[1,3],[2,3],[3,7],[6,6]]
        queries = [2,3,1,7,6,8] 
        ## [(2, 0), (3, 1), (1, 2), (7, 3), (6, 4), (8, 5)]
        ## [(1, 2), (2, 0), (3 ,1), (6, 4), (7, 3), (8, 5)]

        Qlog Q + N logN

        N

        """
        result = [-1] * len(queries)

        intervals.sort(key=lambda x:x[0])

        s_queries = []
        for index, q in enumerate(queries):
            s_queries.append((q, index))
        s_queries.sort(key=lambda x: x[0])

        i = 0
        minheap = []

        for q, index in s_queries:

            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                dist = right - left + 1
                heapq.heappush(minheap, (dist, right))
                i += 1

            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)

            if minheap:
                result[index] = minheap[0][0]

        return result








