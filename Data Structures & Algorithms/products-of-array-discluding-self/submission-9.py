class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []

        N = len(nums)
        
        prefix = 1
        for i in range(N):
            output.append(prefix)
            prefix *= nums[i]

        suffix = 1
        for i in range(N-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output