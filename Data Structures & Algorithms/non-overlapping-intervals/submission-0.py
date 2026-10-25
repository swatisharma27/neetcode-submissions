class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[0])
        N = len(intervals)
        count = 0
        prevEnd = intervals[0][1]

        for i in range(1, N):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            else:
                count += 1
                prevEnd = min(prevEnd, intervals[i][1])

        return count