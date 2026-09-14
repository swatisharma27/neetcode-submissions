class Solution:
    def minWindow(self, s: str, t: str) -> str:
        M = len(t)
        N = len(s)

        if M > N:
            return ""

        tfreq = {}
        for i in range(M):
            tfreq[t[i]] = tfreq.get(t[i], 0) + 1

        need = len(tfreq) # distinct characters
        have = 0

        sfreq = {}
        L = 0
        result = N
        char = ""

        for R in range(N):
            if s[R] in tfreq:
                sfreq[s[R]] = sfreq.get(s[R], 0) + 1
                if sfreq[s[R]] == tfreq[s[R]]:
                    have += 1
            
            while have == need:

                if R-L+1 <= result:
                    result = R-L+1
                    char = s[L:R+1]
                
                if s[L] in tfreq:
                    sfreq[s[L]] -= 1
                    if sfreq[s[L]] < tfreq[s[L]]:
                        have -= 1

                L += 1
        return char




                


            





        