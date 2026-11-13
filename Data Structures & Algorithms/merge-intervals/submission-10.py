class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for interval in intervals[1:]:

            # conflict
            if result[-1][1] >= interval[0]:
                result[-1] = [min(result[-1][0], interval[0]), max(result[-1][1], interval[1])]
            # not conflict:
            else:
                result.append(interval)

        return result

