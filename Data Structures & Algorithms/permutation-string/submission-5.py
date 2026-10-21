class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # edge case
        if len(s1) > len(s2):
            return False

        s1Map = {}
        for i in s1:
            s1Map[i] = s1Map.get(i, 0) + 1

        L = 0
        R = 0
        N = len(s2)

        have = 0
        minLen = float("inf")

        while R < N:
            
            # incoming
            incoming = s2[R]
            if incoming in s1Map:
                s1Map[incoming] -= 1
                if s1Map[incoming] == 0:
                    have += 1

            # outgoing
            if R-L+1 > len(s1):
                outgoing = s2[L]
                if outgoing in s1Map:
                    s1Map[outgoing] += 1
                    if s1Map[outgoing] == 1:
                        have -= 1
                L += 1

            if have == len(s1Map):
                return True

            R += 1
        
        return False

            




        