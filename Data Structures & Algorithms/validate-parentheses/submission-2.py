class Solution:
    def isValid(self, s: str) -> bool:
        """
        TC: O(n)
        SC: O(n) - worst case nothing pops out and all elements enter the stack
        """
        
        st = []        

        for bracket in s:

            # Append the opening bracket
            if bracket == "(" or bracket == "{" or bracket == "[":
                st.append(bracket)

            # Check the top if the closing bracket
            elif bracket == ")":
                if st and st[-1] == "(":
                    st.pop()
                else:
                    return False 

            elif bracket == "}":
                if st and st[-1] == "{":
                    st.pop()
                else:
                    return False

            elif bracket == "]":
                if st and st[-1] == "[":
                    st.pop()
                else:
                    return False

        if len(st) == 0:
            return True
        return False