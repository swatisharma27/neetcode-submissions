class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        st = []

        for element in tokens:

            if element == "+":
                right = int(st.pop())
                left = int(st.pop())
                total = left + right
                st.append(total)
                
            elif element == "-":
                right = st.pop()
                left = st.pop()
                total = left - right
                st.append(total)

            elif element == "*":
                right = st.pop()
                left = st.pop()
                total = left * right
                st.append(total)


            elif element == "/":
                right = st.pop()
                left = st.pop()
                total = int(left / right)
                st.append(total)

            else:
                st.append(int(element))

        return int(st[-1])



