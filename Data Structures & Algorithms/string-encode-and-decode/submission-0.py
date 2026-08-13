class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            length = len(word)
            s += f"{length}#{word}"        
        return s

    def decode(self, s: str) -> List[str]:
        result = []
        N = len(s)
        num = ""
        i = 0
        while i < N:
            if s[i].isdigit():
                while s[i] != "#":
                    num += s[i]
                    i += 1 

                word = s[i+1:i+int(num)+1]
                result.append(word)
                i = i+int(num)+1
                num = ""

        return result