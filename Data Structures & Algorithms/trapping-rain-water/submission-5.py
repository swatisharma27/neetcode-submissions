class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        
        left = 0
        right = N - 1
        leftMax = float("-inf")
        rightMax = float("-inf")
        water = 0

        while left < right:

            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if leftMax <= rightMax:
                water +=  min(leftMax, rightMax) - height[left]
                left += 1
            else:
                water +=  min(leftMax, rightMax) - height[right] 
                right -= 1

        return water