class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        TC: O(n)
        SC: O(n)
        """
        N = len(temperatures)
        st = []

        output = [0] * N

        for i in range(N):
            
            while st and temperatures[i] > temperatures[st[-1]]:
                popped = st.pop()
                output[popped] = i - popped
                
            st.append(i)
            
        return output