class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        TC: O(Nlog N) + O(Qlog Q)
        SC: O(N + Q)
        """

        intervals.sort(key=lambda x:x[0])

        sort_queries = []
        for indx, q in enumerate(queries):
            sort_queries.append([q, indx])

        sort_queries.sort(key=lambda x:x[0])

        result = [-1] * len(queries)
        i = 0
        N = len(intervals)
        minheap = []

        for q, indx in sort_queries:

            while i < N and intervals[i][0] <= q:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(minheap, [length, right])
                i += 1

            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)

            if minheap:
                result[indx] = minheap[0][0]

        return result



       
      