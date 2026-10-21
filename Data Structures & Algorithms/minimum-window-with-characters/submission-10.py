class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        sMap = {}

        for i in t:
            tMap[i] = tMap.get(i, 0) + 1

        need = len(tMap)
        have = 0

        L = 0
        R = 0
        N = len(s)

        minLen = float("inf")
        substring = ""

        if len(t) > len(s):
            return substring

        while R < N:

            # incoming
            incoming = s[R]
            if incoming in tMap:
                sMap[incoming] = sMap.get(incoming, 0) + 1
                if sMap[incoming] == tMap[incoming]:
                    have += 1                

            # outgoing
            while have == need:
                if minLen >= R-L+1:
                    minLen = R-L+1
                    substring = s[L:R+1]

                outgoing = s[L]
                if outgoing in tMap:
                    sMap[outgoing] -= 1
                    if sMap[outgoing] < tMap[outgoing]:
                        have -= 1
                L += 1

            R += 1

        return substring





