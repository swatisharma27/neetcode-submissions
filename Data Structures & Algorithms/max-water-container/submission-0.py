class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)
        low = 0
        right = N - 1
        maxA = 0

        while low < right:

            width = right - low 
            hgt = min(heights[low], heights[right])
            maxA = max(maxA, width * hgt)

            if heights[low] <= heights[right]:
                low += 1
            else:
                right -=1

        return maxA
