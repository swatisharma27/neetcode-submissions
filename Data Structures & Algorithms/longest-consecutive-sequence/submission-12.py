class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        TC: O(1) as we use set otherwise O(n square search time) in array
        SC: O(n) for the set
        """

        newSet = set(nums)
        N = len(newSet)

        result = float("-inf")
        count = 0

        if not newSet:
            return count

        for element in newSet:
            left = element - 1
            if left not in newSet:
                count += 1
                right = element + 1
                while right in newSet:
                    count += 1
                    right += 1
                result = max(result, count)
                count = 0
            else:
                continue

        return result


