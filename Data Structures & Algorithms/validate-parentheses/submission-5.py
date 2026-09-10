class Solution:
    def isValid(self, s: str) -> bool:

        st = []


        for i in s:

            if not st:
                if i==")" or i=="}" or  i=="]":
                    return False

            if i=="(" or i=="{" or  i=="[":
                st.append(i)

            elif st and i == "}":
                if st[-1] != "{":
                    return False
                else:
                    st.pop()
            
            elif st and i == ")":
                if st[-1] != "(":
                    return False
                else:
                    st.pop()

            elif st and i == "]":
                if st[-1] != "[":
                    return False
                else:
                    st.pop()

        if not st:
            return True
        else:
            return False