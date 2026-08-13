from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ## Monotonic Decreasing Queue
        ### -- large elements at the front, small elements at the back

        N = len(nums)
        L = 0

        dq = deque()
        result = []

        for R in range(N):
            # new elements have arrived

            # Remove smaller elements from the back 
            while dq and nums[R] >= nums[dq[-1]] :
                dq.pop()

            # Append the current index
            dq.append(R)

            if dq[0] < L:
                dq.popleft()
            
            # Window reached the size, record maximum, slide left boundary
            if R-L+1 == k:
                result.append(nums[dq[0]])
                L += 1
                
        return result
