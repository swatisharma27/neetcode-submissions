class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[1])
        count = 0

        prevEnd = float("-inf")

        for interval in intervals:
            # no conflict
            if prevEnd <= interval[0]:
                prevEnd = interval[1]
            # conflict
            else:
                count += 1

        return count
