class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n2 < n1:
            nums1, nums2 = nums2, nums1 
            n1, n2 = n2, n1 #len will be updated too

        low = 0
        high = n1 ## Binary search on partition , so not N-1 
        median = 0
        while low <= high:

            partX = low + (high-low)//2
            partY = (n1+n2+1)//2 - partX

            X1 = float("-inf") if partX == 0 else nums1[partX - 1]
            Y1 = float("inf") if partX == n1 else nums1[partX]
            X2 = float("-inf") if partY == 0 else nums2[partY- 1]
            Y2 = float("inf") if partY == n2 else nums2[partY]

            if X1 <= Y2 and X2 <= Y1:
                # we found the median

                if (n1+n2) % 2 == 0:
                    # even - median is avg of two middle elements
                    return (max(X1, X2) + min(Y1, Y2)) / 2

                else:
                    # odd - median is the middle element
                    return max(X1, X2)

            elif X2 > Y1:
                low = partX + 1

            else:
                high = partX - 1
       