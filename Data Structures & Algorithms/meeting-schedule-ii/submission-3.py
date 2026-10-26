"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0

        N = len(intervals)
        intervals.sort(key=lambda x:x.start)

        heap = [intervals[0].end]

        for i in range(1, N):
            if heap[0] <= intervals[i].start:
                heapq.heappop(heap)

            heapq.heappush(heap, intervals[i].end)

        return len(heap)


                



            

        

























        # """
        # TC: O(nlogn)
        # SC: O(n)
        # """
        # if not intervals:
        #     return 0

        # start_lst = []
        # end_lst = []

        # for interval in intervals:
        #     start_lst.append(interval.start)
        #     end_lst.append(interval.end)

        # start_lst.sort()
        # end_lst.sort()

        # s = 0
        # e = 0
        # count = 0
        # result = 0

        # while s < len(start_lst):
        #     if start_lst[s] < end_lst[e]:
        #         count += 1
        #         s += 1
        #     else:
        #         e += 1
        #         count -= 1

        #     result = max(result, count)

        # return result
