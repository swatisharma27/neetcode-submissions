class Solution:
    def maxArea(self, heights: List[int]) -> int:

        N = len(heights)
        low = 0
        high = N - 1
        maxArea = 0

        while low < high:

            width = high - low
            height = min(heights[low], heights[high])
            area = width * height

            maxArea = max(maxArea, area)

            if heights[low] < heights[high]:
                low += 1
            else:
                high -= 1

        return maxArea
        