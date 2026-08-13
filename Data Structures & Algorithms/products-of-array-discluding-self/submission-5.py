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
        suffix_prod = 1

        for i in range(N):
            if i==0:
                result.append(prefix_prod) ## not nums[i] would be output = 1
                prefix_prod = nums[i] 
            else:
                result.append(prefix_prod)
                prefix_prod *= nums[i] 

        for i in range(N-1, -1, -1):
            if i == N-1:
                suffix_prod = nums[i]
            else:
                value = result[i] * suffix_prod
                result[i] = value
                suffix_prod *= nums[i]

        return result
            