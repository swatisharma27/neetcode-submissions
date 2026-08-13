class Solution:
    def minWindow(self, s: str, t: str) -> str:

        N = len(s)
        result = N
        L = 0
        char = ""
        tFreq = {}
        sFreq = {}

        for item in t:
            tFreq[item] = tFreq.get(item, 0) + 1

        need = len(tFreq)
        have = 0

        if need > N:
            return char

        for R in range(N):
            inchar = s[R]
            if inchar in tFreq:
                sFreq[inchar] = sFreq.get(inchar, 0) + 1
                if sFreq[inchar] == tFreq[inchar]:
                    have += 1

            while have == need:
                if R-L+1 <= result:
                    result = R-L+1
                    char = s[L:R+1]

                if s[L] in tFreq:
                    sFreq[s[L]] -= 1
                    if sFreq[s[L]] < tFreq[s[L]]:
                        have -= 1
                L+=1

        return char


        