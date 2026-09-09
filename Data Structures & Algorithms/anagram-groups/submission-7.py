class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq = {}

        for s in strs:

            l = [0] * 26
            for ch in s:
                l[ord(ch)- ord('a')] += 1

            if tuple(l) not in freq:
                freq[tuple(l)] = [s]
            else:
                freq[tuple(l)].append(s)

        return list(freq.values())



                


        