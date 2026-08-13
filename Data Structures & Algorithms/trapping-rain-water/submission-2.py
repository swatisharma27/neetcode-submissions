class Solution:
    def trap(self, height: List[int]) -> int:
        
        N = len(height)

        leftMax = 0
        rightMax = 0

        left = 0
        right = N-1

        water = 0

        while left < right:

            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            
            if leftMax <= rightMax:
                water += leftMax - height[left]
                left += 1
            else:
                water += rightMax - height[right]
                right -=1

        return water

