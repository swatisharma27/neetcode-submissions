class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        st = []
        for item in tokens:

            if item == "+" and st:
                right = st.pop()
                left = st.pop()
                total = left + right
                st.append(total)

            elif item == "*" and st:
                right = st.pop()
                left = st.pop()
                total = left * right
                st.append(total)

            elif item == "/" and st:
                right = st.pop()
                left = st.pop()
                total = int(left / right)
                st.append(total)

            elif item == "-" and st:
                right = st.pop()
                left = st.pop()
                total = left - right
                st.append(total)

            else:
                st.append(int(item))

        return int(st[-1])