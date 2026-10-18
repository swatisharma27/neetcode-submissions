class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        
        for word in strs:
            arr = [0] * 26
            for ch in word:
                indx = ord(ch) - ord('a')
                arr[indx] += 1

            arr = tuple(arr) 
            if arr not in freq:
                freq[arr] = [word]
            else:
                freq[arr].append(word)
            
        return list(freq.values())

            

                
