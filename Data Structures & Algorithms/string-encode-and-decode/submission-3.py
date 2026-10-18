class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            wordLen = len(word)
            result += f"{wordLen}#{word}"

        return result


    def decode(self, s: str) -> List[str]:
        num = ""
        N = len(s)
        result = []
        i = 0
        while i < N:
            while s[i] != "#":
                num += s[i]
                i += 1
            word = s[i+1:i+int(num)+1]
            result.append(word)
            i = i + int(num) + 1
            num = ""
        return result





            


