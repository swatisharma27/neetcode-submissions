# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### ____________ ###
### RECURSIVE DFS ##
### ____________ ###
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ## base
        if root is None:
            return 0

        ## logic
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

### ____________ ###
### ITERATIVE STACK
### ____________ ###
# class Solution:
#     def maxDepth(self, root):

#         ## base
#         if root is None:
#             return 0


#         ## logic
#         st = [[root, 1]]
#         res = 0

#         while st:
#             node, depth = st.pop()
            
#             if node:
#                 res = max(res, depth)
#                 st.append([node.left, depth + 1])
#                 st.append([node.right, depth + 1])

#         return res

class Solution:
    def maxDepth(self, root):
        return self.helper(root)


    def helper(self, root):

        #base
        if root is None:
            return 0


        #logic
        left = self.helper(root.left)
        right = self.helper(root.right)

        return 1+max(left, right)

