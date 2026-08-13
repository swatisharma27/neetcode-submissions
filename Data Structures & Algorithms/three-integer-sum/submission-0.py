class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort the array
        nums.sort()
        N = len(nums)
        result = []

        for i in range(N):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            L = i + 1
            R = N - 1

            while L < R:

                total = nums[i] + nums[L] + nums[R]
                if total == 0:
                    result.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while L < R and nums[L-1] == nums[L]:
                        L += 1

                    while L < R and nums[R] == nums[R+1]:
                        R -= 1
                
                elif total < 0:
                    L += 1

                else:
                    R -=1
        return result
