class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        """
        TC: O(log(min(n1, n2)))
        SC: O(1)
        """
        
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1

        low = 0
        high = n1 #Binary search on partition

        while low <= high:

            partX = mid = low + (high-low)//2
            partY = (n1+n2+1)//2 - partX

            X1 = float("-inf") if partX==0 else nums1[partX-1]
            X2 = float("inf") if partX==n1 else nums1[partX]
            Y1 = float("-inf") if partY==0 else nums2[partY-1]
            Y2 = float("inf") if partY==n2 else nums2[partY]

            if X1 <= Y2 and Y1 <= X2:
                # median can be determined
                if (n1+n2)%2 == 0:
                    # even
                    return (max(X1, Y1) + min(X2, Y2)) / 2
                else:
                    # odd
                    return max(X1, Y1)
                    
            elif X1 > Y2:
                high = mid - 1

            else:
                low = mid + 1
