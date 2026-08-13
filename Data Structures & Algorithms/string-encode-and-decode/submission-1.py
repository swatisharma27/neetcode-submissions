class Solution:

    def encode(self, strs: List[str]) -> str:
        resultStr = ""
        for word in strs:
            lngth = len(word)
            resultStr += f"{lngth}#{word}"
        return resultStr

    def decode(self, s: str) -> List[str]:
        resultArr = []
        N = len(s)
        i = 0
        num = "" 
        while i < N:
            if s[i].isdigit():
                while s[i] != "#":
                    num += s[i]
                    i += 1
            
                left = i + 1
                right = i + 1 + int(num)
                word = s[left: right]
                resultArr.append(word)
                i = right 
                num = ""

        return resultArr
