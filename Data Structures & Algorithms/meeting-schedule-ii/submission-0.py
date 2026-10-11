"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start_lst = []
        end_lst = []

        for interval in intervals:
            start_lst.append(interval.start)
            end_lst.append(interval.end)

        start_lst.sort()
        end_lst.sort()

        s = 0
        e = 0
        count = 0
        result = 0

        while s < len(start_lst):
            if start_lst[s] < end_lst[e]:
                count += 1
                s += 1
            else:
                e += 1
                count -= 1

            result = max(result, count)

        return result








            
        
