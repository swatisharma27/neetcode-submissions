class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        sNums = sorted(nums)
        N = len(sNums)
        result = []

        for i in range(N):

            if i > 0 and sNums[i-1] == sNums[i]:
                continue

            low = i + 1
            high = N - 1

            while low < high:

                total = sNums[i] + sNums[low] + sNums[high]

                if total == 0:
                    result.append([sNums[i], sNums[low], sNums[high]])

                    low += 1
                    high -= 1

                    while low < high and sNums[low-1] == sNums[low]:
                        low += 1

                    while low < high and sNums[high+1] == sNums[high]:
                        high -= 1           

                    #check

                elif total > 0:
                    high -= 1

                else:
                    low += 1

        return result
        