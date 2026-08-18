class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if len(s) != len(t):
            return False

        sMap = {}
        for ch in s:
            sMap[ch] = sMap.get(ch, 0) + 1

        for ch in t:
            sMap[ch] = sMap.get(ch, 0) - 1

        return  all(sMap[ch] == 0 for ch in sMap)
