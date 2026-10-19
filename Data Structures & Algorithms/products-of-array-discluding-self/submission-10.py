class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        output = []

        for i in range(len(nums)):
            output.append(prefix)
            prefix *= nums[i]


        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        
        return output



"""
1, 2, 4, 6

output = [1, 1, 2, 8]

suffix = 1
output[3] = 8 [1,1,2,8]
suffix = 1*nums[3] = 1*6 = 6

output[2] = 6*2 = 12
suffix = 6*nums[2] = 6*4 = 24

output[3] = 24*1 = 24
suffix = 24*nums[1]= 24*2 = 48



"""