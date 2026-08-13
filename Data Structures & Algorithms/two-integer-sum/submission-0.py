class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq= {}
        N = len(nums)

        for i in range(N):
            value = target - nums[i]
            if (target - nums[i]) in freq:
                return [freq[value], i]
            else:
                freq[nums[i]] = i
