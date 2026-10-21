class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minLen = float("inf")
        substring = ""

        # edge case
        if len(t) > len(s):
            return substring

        tFreq = {}
        sFreq = {}

        for i in t:
            tFreq[i] = tFreq.get(i, 0) + 1

        L = 0
        R = 0
        N = len(s)

        need = len(tFreq)
        have = 0

        while R < N:

            # incoming
            incoming = s[R]
            if incoming in tFreq:
                sFreq[incoming] = sFreq.get(incoming, 0) + 1
                if sFreq[incoming] == tFreq[incoming]:
                    have += 1

            # outgoing
            while have == need:

                if minLen >= R-L+1:
                    minLen = R-L+1
                    substring = s[L:R+1]

                outgoing = s[L]
                if outgoing in tFreq:
                    sFreq[outgoing] -= 1
                    if sFreq[outgoing] < tFreq[outgoing]:
                        have -= 1
                L += 1

            R += 1
        return substring