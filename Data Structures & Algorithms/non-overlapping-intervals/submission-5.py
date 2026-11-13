class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[1])
        count = 0

        prevEnd = float("-inf")

        for interval in intervals:
            if interval[0] >= prevEnd:
                prevEnd = interval[1]
            else:
                count += 1

        return count




















