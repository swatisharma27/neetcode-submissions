class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        TC: O(N*M)
        SC: O(1)
        """

        M = len(s1) # small
        N = len(s2) # big 
        match = 0
        
        if M > N:
            return False

        freq = {}
        for i in s1:
            freq[i] = freq.get(i, 0) + 1

        for R in range(N):

            # incoming
            in_char = s2[R]
            if in_char in freq:
                freq[in_char] -= 1
                if freq[in_char] == 0:
                    match += 1

            # outgoing 
            if R >= M:
                out_char = s2[R-M]
                if out_char in freq:
                    freq[out_char] += 1
                    if freq[out_char] == 1:
                        match -= 1

            if match == len(freq):
                return True

        return False

        