class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        TC: O(n+m)
        SC: O(1)
        """

        N = len(s)
        M = len(t)
        result = ""
        minimum = N

        if M > N:
            return result

        tMap ={}
        need = 0
        for item in t:
            tMap[item] = tMap.get(item, 0) + 1
        need = len(tMap)

        sMap = {}
        have = 0
        #incoming    
        L = 0
        for R in range(N):
            inchar = s[R]
            if inchar in tMap:
                sMap[inchar] = sMap.get(inchar, 0) + 1
                if sMap[inchar] == tMap[inchar]:
                    have += 1

            while have == need:
                if (R-L+1) <= minimum:
                    minimum = R-L+1
                    result = s[L: R+1]
                
                outchar = s[L]
                if outchar in tMap:
                    sMap[outchar] -= 1
                    if sMap[outchar] < tMap[outchar]:
                        have -= 1

                L += 1


        return result


        

        











































































# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         """
#         TC: O(n+m)
#         SC: O(1)
#         """

#         N = len(s)
#         result = N
#         L = 0
#         char = ""
#         tFreq = {}
#         sFreq = {}

#         for item in t:
#             tFreq[item] = tFreq.get(item, 0) + 1

#         need = len(tFreq)
#         have = 0

#         if len(t) > N:
#             return char

#         for R in range(N):
#             inchar = s[R]
#             if inchar in tFreq:
#                 sFreq[inchar] = sFreq.get(inchar, 0) + 1
#                 if sFreq[inchar] == tFreq[inchar]:
#                     have += 1

#             while have == need:
#                 if R-L+1 <= result:
#                     result = R-L+1
#                     char = s[L:R+1]

#                 if s[L] in tFreq:
#                     sFreq[s[L]] -= 1
#                     if sFreq[s[L]] < tFreq[s[L]]:
#                         have -= 1
#                 L+=1

#         return char
        