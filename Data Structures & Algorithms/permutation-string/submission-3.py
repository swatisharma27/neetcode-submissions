class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq = {}
        M = len(s1)

        L = 0
        R = 0
        N = len(s2)

        if M > N:
            return False

        for i in range(M):
            freq[s1[i]] = freq.get(s1[i], 0) + 1

        while R < N:

            if s2[R] in freq:
                freq[s2[R]] -= 1

            if (R-L+1) > M:
                if s2[L] in freq:
                    freq[s2[L]] += 1
                L += 1

            if (R-L+1) == M:
                if all(i==0 for i in freq.values()):
                    return True
        
            R += 1
        return False
                

                 
        