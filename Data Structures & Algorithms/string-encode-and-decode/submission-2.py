class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for word in strs:
            lngth = len(word)
            out += f"{lngth}#{word}"

        return out

    def decode(self, s: str) -> List[str]:
        
        result = []
        N = len(s)
        i = 0
        out = ""

        while i < N:
            if s[i].isdigit():
                while s[i] != "#":
                    out += s[i]
                    i += 1
                result.append(s[i+1:i+int(out)+1])
                i = i+int(out)+1
                out = ""
        return result
