class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        st = [-1]
        heights.append(0)
    
        maxArea = 0
        N = len(heights)
        
        for i in range(N):
            while st != [-1] and heights[i] < heights[st[-1]]:
                h_index = st.pop()
                w = i - st[-1] - 1

                area = heights[h_index] * w
                maxArea = max(maxArea, area)

            st.append(i)


        return maxArea




        
