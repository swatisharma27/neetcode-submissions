class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        result = [-1] * len(queries)

        intervals.sort()

        sortedQueries = [] 
        for idx, q in enumerate(queries):
            sortedQueries.append([q, idx])
        sortedQueries.sort(key=lambda x:x[0])

        heap = []
        i = 0
        for q, idx in sortedQueries:

            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(heap, (length, right))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                result[idx] = heap[0][0]

        return result



            