class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        TC: O(log n)
        SC: O(1)
        """

        N = len(nums)
        low = 0 
        high = N - 1

        while low <= high:
            mid = low + (high-low) // 2

            if nums[mid] == target:
                return mid
            
            # left sorted
            elif nums[low] <= nums[mid]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # right sorted
            # elif nums[M] <= nums[H]:
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

            
        return - 1
