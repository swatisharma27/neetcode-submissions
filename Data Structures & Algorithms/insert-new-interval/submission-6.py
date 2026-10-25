class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        TC: O(n)
        SC: O(n)
        """
        # if not intervals and newInterval:
        #     return newInterval

        N = len(intervals)
        result = []

        for i in range(N):

            # beginning
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            
            # end
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                
        result.append(newInterval)
        return result




