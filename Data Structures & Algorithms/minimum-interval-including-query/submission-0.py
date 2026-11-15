class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        result = [-1] * len(queries)

        intervals.sort()

        sortedQueries = []
        for idx, q in enumerate(queries):
            sortedQueries.append((q, idx))
        sortedQueries.sort(key=lambda x:x[0])

        minheap = []
        i = 0
        N = len(intervals)

        for q, index in sortedQueries:
            while i < N and intervals[i][0] <= q:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(minheap, (length, right))
                i += 1

            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)

            if minheap:
                result[index] = minheap[0][0]

        return result

            