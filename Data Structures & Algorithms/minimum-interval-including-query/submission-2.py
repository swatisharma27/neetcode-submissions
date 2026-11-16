class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
       
        intervals.sort()

        sort_queries = []
        for indx, q in enumerate(queries):
            sort_queries.append((q,indx))

        sort_queries.sort(key=lambda x:x[0])
        i = 0
        N = len(intervals)

        result = [-1] * len(queries)
        heap = []

        for q, index in sort_queries:
            while i < N and intervals[i][0] <= q:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(heap, (length, right))
                i += 1
            
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                result[index] = heap[0][0]

        return result





