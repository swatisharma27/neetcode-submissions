class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []
        N = len(intervals)


        for i in range(N):

            # newInterval before current
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            
            # newInterval before current
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            # overlap - merge
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        result.append(newInterval)
        return result

        
