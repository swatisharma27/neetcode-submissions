class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        low = 0 
        high = len(heights) - 1
        maxArea = 0

        while low < high:

            length = high - low
            height = min(heights[low], heights[high])
            area = length * height
            maxArea = max(area, maxArea)

            if heights[low] < heights[high]:
                low += 1
            else:
                high -= 1
            
        return maxArea
