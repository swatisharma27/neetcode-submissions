class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        L = 0
        R = 0
        N = len(s)
        output = 0
        freq = {}


        while R < N:

            if s[R] in freq:
                L = max(L, freq[s[R]]+1)

            freq[s[R]] = R
            output = max(output, R-L+1)
            R += 1

        return output        