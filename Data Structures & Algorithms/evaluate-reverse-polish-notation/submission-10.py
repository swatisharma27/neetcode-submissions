class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if not tokens or len(tokens) == 0:
            return 
        
        st = []

        for element in tokens:

            if st and element == "+":
                right = int(st.pop())
                left = int(st.pop())
                total = left + right
                st.append(total)
                
            elif st and element == "-":
                right = int(st.pop())
                left = int(st.pop())
                total = left - right
                st.append(total)

            elif st and element == "*":
                right = int(st.pop())
                left = int(st.pop())
                total = left * right
                st.append(total)


            elif st and element == "/":
                right = int(st.pop())
                left = int(st.pop())
                total = int(left / right)
                st.append(total)

            else:
                st.append(element)

        return int(st[-1])



