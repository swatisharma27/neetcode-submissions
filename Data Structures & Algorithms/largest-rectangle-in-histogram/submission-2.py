class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        TC: O(2n) ## pop and push once each element
        SC: O(n)
        """

        heights.append(0)

        st = [-1] #Sentinel index
        maxArea = 0

        N = len(heights)

        for i in range(N):
            while st != [-1] and heights[i] < heights[st[-1]]:
                popped = st.pop()
                area = heights[popped] * (i - st[-1] -1) ## (right smaller - left smaller - 1)
                maxArea = max(area, maxArea)

            st.append(i)

        return maxArea
