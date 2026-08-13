class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        TC: O(n)
        SC: O(1)
        """   
        L = 0
        result = 0
        freq = {}
        N = len(s)

        maxF = 0

        for R in range(N):
            freq[s[R]] = freq.get(s[R], 0) + 1
            maxF = max(freq.values())

            while (R-L+1) - maxF > k:
                freq[s[L]] -= 1
                L += 1

            result = max(result, R-L+1)

        return result
 