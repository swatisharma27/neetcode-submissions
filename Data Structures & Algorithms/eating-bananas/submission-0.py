from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        TC: O(n*log(max(piles)-1+1)) = O(n*log(max(piles))) >> n: each iteration scans all n piles
        SC: O(1)
        """
        low = 1 #min 1 banana
        high = max(piles) #max banana koko can eat in hour

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
