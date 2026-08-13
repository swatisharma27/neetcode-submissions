class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Brute Force: 
            TC: O(n^2)
            SC: O(1)

        Optimal Solution:
            TC: O(n)
            SC: O(1)

        """
        
        N = len(nums)
        result = []

        prefix_prod = 1
        for i in range(N):
            result.append(prefix_prod) 
            prefix_prod *= nums[i] 

        suffix_prod = 1
        for i in range(N-1, -1, -1):
            result[i] *= suffix_prod
            suffix_prod *= nums[i]

        return result
            