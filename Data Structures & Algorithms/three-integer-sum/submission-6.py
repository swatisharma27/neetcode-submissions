class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        for i in range(len(nums)):

            if i > 0 and nums[i-1] == nums[i]:
                continue

            low = i + 1
            high = len(nums) - 1

            while low < high:

                total = nums[i] + nums[low] + nums[high]

                if total == 0:
                    result.append([nums[i], nums[low], nums[high]])

                    low += 1
                    high -= 1

                    while low < high and nums[low-1] == nums[low]:
                        low += 1

                    while low < high and nums[high] == nums[high+1]:
                        high -= 1

                elif total > 0:
                    high -= 1

                else:
                    low += 1
        return result            

        