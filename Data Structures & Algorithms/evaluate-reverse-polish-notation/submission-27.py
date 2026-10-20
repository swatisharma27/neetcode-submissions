class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for i in tokens:
            
            if i == "+":
                right = int(st.pop())
                left = int(st.pop())
                total = left + right
                st.append(total)

            elif i == "-":
                right = int(st.pop())
                left = int(st.pop())
                total = left - right
                st.append(total)

            elif i == "*":
                right = int(st.pop())
                left = int(st.pop())
                total = left * right
                st.append(total) 

            elif i == "/":
                right = int(st.pop())
                left = int(st.pop())
                total = int(left / right)
                st.append(total)

            else:
                st.append(i)

        return int(st[-1])




        