class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)

        L = 0
        R = 0

        freq = {}
        output = 0
        maxF = 0

        while R < N:

            freq[s[R]] = freq.get(s[R], 0) + 1
            maxF = max(maxF, freq[s[R]])

            while (R-L+1) - maxF > k:
                freq[s[L]] -= 1
                L += 1

            output = max(output, R-L+1)
            R += 1

        return output
