class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        new = set()
        for i in nums:
            if i in new:
                return True
            else:
                new.add(i)
        return False

