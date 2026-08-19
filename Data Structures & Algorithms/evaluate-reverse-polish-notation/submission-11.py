class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        TC: O(n)
        SC: O(n)
        """

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
#         if not tokens or len(tokens) == 0:
#             return 
        
#         st = []

#         for element in tokens:

#             if st and element == "+":
#                 right = int(st.pop())
#                 left = int(st.pop())
#                 total = left + right
#                 st.append(total)
                
#             elif st and element == "-":
#                 right = int(st.pop())
#                 left = int(st.pop())
#                 total = left - right
#                 st.append(total)

#             elif st and element == "*":
#                 right = int(st.pop())
#                 left = int(st.pop())
#                 total = left * right
#                 st.append(total)


#             elif st and element == "/":
#                 right = int(st.pop())
#                 left = int(st.pop())
#                 total = int(left / right)
#                 st.append(total)

#             else:
#                 st.append(element)

#         return int(st[-1])



