class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        """
        TC: O(n)
        SC: O(n)
        """

        result = [0] * len(temperatures)
        N = len(result)
        st = []

        for i in range(N):
            while st and temperatures[i] > temperatures[st[-1]]:
                result [st[-1]] = i - st[-1]
                st.pop()

            st.append(i)


        return result

        