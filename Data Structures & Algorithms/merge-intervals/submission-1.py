class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        TC: O(nlogn)
        SC: O(n)
        """

        intervals.sort()

        result = [intervals[0]]

        for i in intervals[1:]:
            if result[-1][1] >= i[0]:
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result.append(i)

        return result


            
        