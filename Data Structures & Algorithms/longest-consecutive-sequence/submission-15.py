class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = 1
        i = 0
        N = len(nums)
        result = 0

        for num in nums:
            prev = num - 1
            if prev not in nums_set:
                next_curr = num + 1
                while next_curr in nums_set:
                    count += 1
                    next_curr += 1
                result = max(result, count)
                count = 1
        return result
            

