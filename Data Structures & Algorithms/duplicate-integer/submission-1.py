class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # freq = {}
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
        #     if freq[num] > 1:
        #         return True
        # return False  


        freq = set()
        for num in nums:
            if num in freq:
                return True
            else:
                freq.add(num)
        return False      