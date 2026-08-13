class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        TC: O(n^2)
        SC: O(1)
        """

        # sort the array - O(nlogn)
        nums.sort()

        N= len(nums)

        result = []

        for i in range(N):

            if i > 0 and nums[i-1] == nums[i]:
                continue

            low = i + 1
            high = N - 1

            while low < high:

                total = nums[i] + nums[low] + nums[high]

                if total == 0:
                    result.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1

                    while low < high and nums[low-1] == nums[low]:
                        low += 1

                    while low < high and nums[high+1] == nums[high]:
                        high -=1
                
                elif total < 0:
                    low += 1
                
                else:
                    high -= 1

        return result



        


