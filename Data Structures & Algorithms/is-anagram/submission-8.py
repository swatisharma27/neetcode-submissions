class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sMap = {}
        for i in s:
            sMap[i] = sMap.get(i, 0) + 1

        for i in t:
            sMap[i] = sMap.get(i, 0) - 1
        
        return all(i==0 for i in list(sMap.values()))