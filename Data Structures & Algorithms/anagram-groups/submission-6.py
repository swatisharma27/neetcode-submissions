class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        TC: O(nk)
        SC: O(nk)
        """
        resultDict = {}
        for s in strs:

            arr = [0] * 26
            for ch in s:
                arr[ord(ch) - ord('a')] += 1

            resultDict.setdefault(tuple(arr), []).append(s)

        return list(resultDict.values())