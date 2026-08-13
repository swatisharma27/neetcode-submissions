# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

#         """
#         TC: O(n)
#         SC: O(n)
#         """

#         freq = {}

#         if len(s) != len(t):
#             return False

#         for ch in s: 
#             freq[ch] = freq.get(ch, 0) + 1

#         for char in t:
#             if char not in freq:
#                 return False
#             freq[char] -= 1

#         return all(value == 0 for char in freq.values())


## now to reduce SC: O(n) to O(1)
##### ARRAY OF FREQUENCY 26 #####
class Solution:
    def isAnagram(self, s, t):
        freq = [0] * 26 #26 characters

        if len(s) != len(t):
            return False

        for char in s:
            freq[ord(char) - ord('a')] += 1

        for char in t:
            freq[ord(char) - ord('a')] -= 1

        return all(num==0 for num in freq)


        





