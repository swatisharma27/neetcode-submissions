class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        TC: O(log n)
        SC: O(1)
        """

        N = len(nums)
        low = 0
        high = N - 1

        while low <= high:

            ## Array is sorted in ascending order 
            if nums[low] <= nums[high]:
                return nums[low]

            mid = low + (high - low)// 2
            # Check neighboring elements
            # if num[mid] is less than both the left and right neighboring
            if (mid == 0 or nums[mid] < nums[mid -1]) and (mid == N-1 or nums[mid] < nums[mid+1]) :
                return nums[mid]

            ## Left sorted
            # min pivot will be on the right side
            elif nums[low] <= nums[mid]:
                low = mid + 1
            

            ## Right sorted
            # min pivot will be on the left side
            # elif nums[low] <= nums[mid]:
            else:
                high = mid - 1

        return -1
