class Solution:
    def trap(self, height: List[int]) -> int:

        N = len(height)

        L = 0
        R = N-1
        leftmax = height[L]
        rightmax = height[R]

        water = 0
        
        while L < R:

            leftmax = max(leftmax, height[L])
            rightmax = max(rightmax, height[R])

            if leftmax <= rightmax:
                if height[L] <= leftmax:
                    water += leftmax -  height[L]
                L += 1
            else:
                if height[R] < rightmax:
                    water += rightmax - height[R]
                R -= 1
        return water

