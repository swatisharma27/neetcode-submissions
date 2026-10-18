class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        freq = {}

        for idx in range(len(nums)):
            complement = target - nums[idx]
            if complement not in freq:
                freq[nums[idx]] = idx
            else:
                return [freq[complement], idx]
