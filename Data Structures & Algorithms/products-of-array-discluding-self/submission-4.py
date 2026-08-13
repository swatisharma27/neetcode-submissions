class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Brute Force: 
            TC: O(n^2)
            SC: O(n)

        Optimal Solution:
            TC: O(n)
            SC: O(n)

        """
        
        N = len(nums)
        result = []

        output = 1

        for i in range(N):
            if i==0:
                result.append(output) ## not nums[i] would be output = 1
                output = nums[i] 
            else:
                result.append(output)
                output = nums[i] * output

        for i in range(N-1, -1, -1):
            if i == N-1:
                output = nums[i]
            else:
                value = result[i] * output
                result[i] = value
                output = nums[i] * output

        return result
            
