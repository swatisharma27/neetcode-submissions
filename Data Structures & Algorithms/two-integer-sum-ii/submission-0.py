class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        TC: O(n)
        SC: O(1)
        """

        N = len(numbers)
        L = 0
        R = N-1

        while L < R:
            total = numbers[L] + numbers[R]

            if total == target:
                return [L+1,R+1]
            elif total < target:
                L += 1
            else:
                R -= 1
        