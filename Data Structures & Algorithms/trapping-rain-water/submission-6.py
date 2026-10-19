class Solution:
    def trap(self, height: List[int]) -> int:
        
        low = 0
        high = len(height) - 1
        
        leftMax = 0
        rightMax = 0

        water = 0

        while low < high:
            
            if height[low] <= height[high]:

                if height[low] >= leftMax:
                    leftMax = height[low]
                else:
                    water += leftMax - height[low]
                
                low += 1
            
            else:

                if height[high] >= rightMax:
                    rightMax = height[high]
                     
                else:
                    water += rightMax - height[high]
                
                high -= 1

        return water

