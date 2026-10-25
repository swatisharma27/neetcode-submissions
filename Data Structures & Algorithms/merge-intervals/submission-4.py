class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        TC: O(nlogn)
        SC: O(n)
        """

        intervals.sort(key=lambda x:x[0])
        N = len(intervals)

        result = [intervals[0]]

        for i in range(1, N):

            # overlap
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                # non-overlap
                result.append(intervals[i])

        return result






























        # intervals.sort()

        # result = [intervals[0]]

        # for i in intervals[1:]:
        #     if result[-1][1] >= i[0]:
        #         result[-1][1] = max(result[-1][1], i[1])
        #     else:
        #         result.append(i)

        # return result
