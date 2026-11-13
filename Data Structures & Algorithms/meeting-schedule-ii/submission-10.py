"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x: x.start)
        minheap = []

        for interval in intervals:

            # not conflict
            if minheap and interval.start >= minheap[0]:
                heapq.heappop(minheap)

            # conflict
            heapq.heappush(minheap, interval.end)
        
        return len(minheap)




intervals=[(1,5),(5,10),(10,15),(15,20)]


# 1, 5
# minheap = [5]

# 5, 10
# minheap, 5 >= 5 , no 
# minheap = [10]

# 10, 15
# minheap, 10 >= 10, no
# minheap = [15]


# 15, 20
# minheap, 15 >= 15, no
# minheap = [20]





























        # if not intervals:
        #     return 0

        # N = len(intervals)
        # intervals.sort(key=lambda x:x.start)
        # result = [0] * N

        # heap = [intervals[0].end]
        # result[0] = 1
        # count = 1

        # for i in range(1, N):
        #     while heap and heap[0] <= intervals[i].start:
        #         heapq.heappop(heap)
        #         count -= 1

        #     heapq.heappush(heap, intervals[i].end)
        #     count += 1
        #     result[i] = count
        
        # return result


                



            

        

























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
