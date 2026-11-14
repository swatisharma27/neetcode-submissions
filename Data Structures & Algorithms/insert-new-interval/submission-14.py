class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []
        N = len(intervals)

        for i in range(N):

            # newInterval is before curr
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]

            # newInterval is after curr
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            # overlap - merge and create a newInterval
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        result.append(newInterval)

        return result
            