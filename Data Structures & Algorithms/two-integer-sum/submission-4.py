class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        freq = {}
        N = len(nums)
        for i in range(N):
            
            complement = target - nums[i]
            if complement not in freq:
                freq[nums[i]] = i
            else:
                return [freq[complement], i]
