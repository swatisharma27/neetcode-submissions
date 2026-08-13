class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []

        prefixProd = 1
        for num in nums:
            result.append(prefixProd)
            prefixProd *= num

        suffixProd = 1
        N = len(nums)
        for i in range(N-1, -1, -1):
            result[i] *= suffixProd
            suffixProd *= nums[i]

        return result
        