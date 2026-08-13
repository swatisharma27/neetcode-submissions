class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        set_nums = set(nums) 
        result = 0
        count = 1

        for num in nums:
            left = num - 1
            if left not in set_nums:
                right = num + 1
                while right in set_nums:
                    count += 1
                    right += 1
                result = max(result, count)
                count = 1
            
        return result