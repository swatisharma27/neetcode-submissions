"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda x:x.start) 

        prevEnd = float("-inf")

        for interval in intervals:
            # conflict
            if interval.start < prevEnd:
                return False
            # no conflict
            else:
                prevEnd = interval.end

        return True
