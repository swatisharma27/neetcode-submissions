class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        N = len(temperatures)
        result = [0] * (N)

        st  = []
        for i in range(N):

            while st and temperatures[st[-1]] < temperatures[i]:
                diff = i - st[-1]
                result[st[-1]] = diff
                st.pop()
            
            st.append(i)
            
        return result