
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        TC: O(M+N) >> O(N)
        SC: O(26) >> O(1)
        """

        M = len(s1)
        N = len(s2)

        if M > N:
            return False

        # put s1 in hashmap
        freq = {}
        for item in s1:
            freq[item] = freq.get(item, 0) + 1

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
                outchar = s2[R-M]
                if outchar in freq:
                    freq[outchar] += 1
                    if freq[outchar] == 1:
                        have -=1
                L += 1

            #match
            if have == len(freq):
                return True

        return False

















































# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         """
#         TC: O(M+N) == O(N)
#         SC: O(1)
#         """
#         M = len(s1) # small
#         N = len(s2) # big 
#         match = 0
        
#         if M > N:
#             return False

#         freq = {}
#         for i in s1:
#             freq[i] = freq.get(i, 0) + 1

#         for R in range(N):

#             # incoming
#             in_char = s2[R]
#             if in_char in freq:
#                 freq[in_char] -= 1
#                 if freq[in_char] == 0:
#                     match += 1

#             # outgoing 
#             if R >= M:
#                 out_char = s2[R-M]
#                 if out_char in freq:
#                     freq[out_char] += 1
#                     if freq[out_char] == 1:
#                         match -= 1

#             if match == len(freq):
#                 return True

#         return False

        