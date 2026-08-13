class Solution:
    def isValid(self, s: str) -> bool:
        
        st = []

        for ch in s:

            if ch=="(" or ch=="{" or ch=="[":
                st.append(ch)

            elif ch=="}":
                if st and st[-1] == "{":
                    st.pop()
                else:
                    return False

            elif ch==")":
                if st and st[-1] == "(":
                    st.pop()
                else:
                    return False

            elif ch=="]":
                if st and st[-1] == "[":
                    st.pop()
                else:
                    return False

        if len(st) == 0:
            return True
        else:
            return False