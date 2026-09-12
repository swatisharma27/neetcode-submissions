class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        N = len(nums)
        low = 0
        high = N-1

        while low <= high:

            if nums[low] <= nums[high]:
                return nums[low]

            mid = low + (high-low)//2

            if (mid == 0 or nums[mid-1] > nums[mid]) and (mid == N-1 or nums[mid+1] > nums[mid]):
                return nums[mid]

            elif nums[low] <= nums[mid]:
                low = mid + 1

            else:
                high = mid - 1

        return -1



