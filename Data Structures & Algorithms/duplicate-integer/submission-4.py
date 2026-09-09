class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        newSet = set()
        
        for i in nums:
            if i in newSet:
                return True
            else:
                newSet.add(i)

        return False

