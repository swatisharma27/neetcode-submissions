class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        st = []
        N = len(temperatures)

        output = [0 for _ in range(N)]
        i = 0

        while i < N:
        
            while st and temperatures[i] > temperatures[st[-1]]:
                output[st[-1]] = i - st[-1] 
                st.pop()
            
            st.append(i)
            i += 1
        
        return output
        