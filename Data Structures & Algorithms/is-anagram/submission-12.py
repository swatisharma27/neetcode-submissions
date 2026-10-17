class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}

        if len(s) != len(t):
            return False

        for ch in s:
            sMap[ch] = sMap.get(ch, 0) + 1

        for ch in t:
            sMap[ch] = sMap.get(ch, 0) - 1

        return all(v == 0 for v in sMap.values())

        