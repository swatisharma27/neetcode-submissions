class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        st = []

        for s in tokens:

            if s == "+" :
                right = st.pop()
                left = st.pop()
                result = left + right
                st.append(result)

            elif s == "-" :
                right = st.pop()
                left = st.pop()
                result = left - right
                st.append(result)

            elif s == "*": 
                right = st.pop()
                left = st.pop()
                result = left * right
                st.append(result)
                
            elif s == "/":
                right = st.pop()
                left = st.pop()
                result = int(left / right)
                st.append(result)

            else:    
                st.append(int(s))


        return st[0]
