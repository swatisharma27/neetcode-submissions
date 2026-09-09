class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq = {}

        for s in strs:

            l = [0] * 26
            for ch in s:
                l[ord(ch)- ord('a')] += 1

            # freq.setdefault(key, default_value).append(value)
            freq.setdefault(tuple(l), []).append(s)

        return list(freq.values())



                


        