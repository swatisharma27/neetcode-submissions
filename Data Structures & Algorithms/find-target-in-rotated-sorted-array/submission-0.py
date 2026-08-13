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
            mid = low + (high-low)//2
            
            # mid is the target
            if nums[mid] == target:
                return mid

            elif nums[low] <= nums[mid]: #LEFT sorted
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # elif nums[mid] <= num [high]:
            else: #RIGHT sorted
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1 
