from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = max(piles)

        while low <= high:
            mid = low + (high-low)//2

            currHour = 0
            for i in range(len(piles)):
                currHour += ceil(piles[i]/mid)

            if currHour <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low
