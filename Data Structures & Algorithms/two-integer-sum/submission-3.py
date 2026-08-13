class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        N = len(nums)
        tempDict = {}
        for i in range(N):
            complement = target - nums[i]
            if complement not in tempDict:
                tempDict[nums[i]] = i
            else:
                return [tempDict[complement], i]
