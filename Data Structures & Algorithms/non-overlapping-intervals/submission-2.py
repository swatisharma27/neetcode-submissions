class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        count = 0
        intervals.sort(key=lambda x:x[1])

        prevEnd = intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] >= prevEnd:
                prevEnd = interval[1]
            else:
                count += 1

        return count 






























        # intervals.sort(key=lambda x:x[0])
        # N = len(intervals)
        # count = 0
        # prevEnd = intervals[0][1]

        # for i in range(1, N):
        #     if intervals[i][0] >= prevEnd:
        #         prevEnd = intervals[i][1]
        #     else:
        #         count += 1
        #         prevEnd = min(prevEnd, intervals[i][1])

        # return count