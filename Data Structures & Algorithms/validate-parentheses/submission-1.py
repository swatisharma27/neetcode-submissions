class Solution:
    def isValid(self, s: str) -> bool:
        
        st = []        

        for bracket in s:

            # Append the opening bracket
            if bracket == "(" or bracket == "{" or bracket == "[":
                st.append(bracket)

            # Check the top if the closing bracket
            if bracket == ")":
                if st and st[-1] == "(":
                    st.pop()
                else:
                    return False 

            if bracket == "}":
                if st and st[-1] == "{":
                    st.pop()
                else:
                    return False

            if bracket == "]":
                if st and st[-1] == "[":
                    st.pop()
                else:
                    return False

        if len(st) == 0:
            return True
        return False