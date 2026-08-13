class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        N = len(nums)
        numsSet = set(nums)
        
        longest = 0

        for num in nums:
            left = num - 1
            if left not in numsSet:
                count = 1
                right = num + 1
                while right in numsSet:
                    count += 1
                    right += 1
                longest = max(longest, count)
                count = 1
        return longest