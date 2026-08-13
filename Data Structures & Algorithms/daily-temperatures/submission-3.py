class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        st = [] ## monotonic decreasing order stack

        N = len(temperatures)
        output = [0 for _ in range(N)]

        for t in range(N):
            while st and temperatures[st[-1]] < temperatures[t]:
                output[st[-1]] = t - st[-1]
                st.pop()
                
            st.append(t)

        return output
