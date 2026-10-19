class Solution:
    def isValid(self, s: str) -> bool:

        st = []


        for ch in s:

            if ch == "[" or ch == "{" or ch == "(":
                st.append(ch)

            elif ch == "]":
                if st:
                    top = st.pop()
                    if top != "[":
                        return False
                    else:
                        continue
                else:
                    return False
            
            elif ch == ")":
                if st:
                    top = st.pop()
                    if top != "(":
                        return False
                    else:
                        continue
                else:
                    return False


            elif ch == "}":
                if st:
                    top = st.pop()
                    if top != "{":
                        return False
                    else:
                        continue
                else:
                    return False   

        if not st:
            return True
        return False
