class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        N = len(nums)
        numsSet = set(nums)
        count = 1
        maxLength = 0

        for num in nums:
            left = num - 1
            if left not in numsSet:
                right = num + 1
                while right in numsSet:
                    count += 1
                    right += 1
                maxLength = max(maxLength, count)
                count = 1
        return maxLength