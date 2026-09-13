class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        TC: O(n)
        SC: O(1)
        """
        M = len(s1)
        N = len(s2)
        
        if M > N:
            return False

        freq = {}
        for i in range(M):
            freq[s1[i]] = freq.get(s1[i], 0) + 1

        L = 0
        have = 0

        for R in range(N):

            #incoming
            inchar = s2[R]
            if inchar in freq:
                freq[inchar] -= 1
                if freq[inchar] == 0:
                    have += 1

            #outgoing
            if (R-L+1) > M:
                outchar = s2[L]
                if outchar in freq:
                    freq[outchar] += 1
                    if freq[outchar] == 1:
                        have -= 1
                L += 1

            if have == len(freq):
                return True
        return False
                

                 
        