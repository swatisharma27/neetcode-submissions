class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[1])
        prevEnd = float("-inf")
        count = 0

        for interval in intervals:
            # no conflict
            if interval[0] >= prevEnd:
                prevEnd = interval[1]   
            else:
                count += 1

        return count