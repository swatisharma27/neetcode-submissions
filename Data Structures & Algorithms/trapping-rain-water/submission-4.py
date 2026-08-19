class Solution:
    def trap(self, height: List[int]) -> int:
        """
        TC: O(n)
        SC: O(1)
        """

        N = len(height)
        L = 0 
        R = N-1   
        leftMax = height[L]
        rightMax = height[R]

        waterTrap = 0

        while L < R:
                        
            if leftMax <= rightMax:
                waterTrap += leftMax - height[L]
                L += 1
                leftMax = max(leftMax, height[L])

            else:
                waterTrap += rightMax - height[R]
                R -= 1
                rightMax = max(rightMax, height[R])

        return waterTrap
        