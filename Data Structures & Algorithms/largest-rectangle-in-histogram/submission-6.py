class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.append(0)
        st = [-1]
        i = 0
        maxArea = 0

        N = len(heights)
        while i < N:
            while st[-1] != -1 and heights[i] < heights[st[-1]]:
                popped = st.pop()
                height = heights[popped]
                width = i - st[-1] - 1
                area = height * width

                maxArea = max(area, maxArea)
            
            st.append(i)
            i += 1
        
        return maxArea