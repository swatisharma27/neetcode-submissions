class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        st = []

        for i in tokens:

            if st and i == "+":
                right = st.pop()
                left = st.pop()
                total = left + right
                st.append(total)

            elif st and i == "*":
                right = st.pop()
                left = st.pop()
                total = left * right
                st.append(total)

            elif st and i == "-":
                right = st.pop()
                left = st.pop()
                total = left - right
                st.append(total)

            elif st and i == "/":
                right = st.pop()
                left = st.pop()
                total = int(left / right)
                st.append(total)

            else:
                st.append(int(i))

        if st:
            return st.pop()

        