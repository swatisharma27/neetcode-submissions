class Solution:
    def search(self, nums: List[int], target: int) -> int:

        N = len(nums)
        L = 0 
        H = N - 1

        while L <= H:

            mid = L + (H-L)//2

            if nums[mid] == target:
                return mid

            elif target < nums[mid]: 
                H = mid - 1

            else:
                L = mid + 1

        return -1