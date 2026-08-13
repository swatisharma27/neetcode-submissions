class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        HashMap + Sliding Window solution
        TC: O(n)
        AS: O(1)
        """

        L = 0
        R = 0
        result = 0
        freq = {}
        N = len(s)

        # while R < N:
        for R in range(N):

            if s[R] in freq:
                L = max(L, freq[s[R]]+1)


            freq[s[R]] = R
            result = max(result, R-L+1)
            # R += 1

        return result 

