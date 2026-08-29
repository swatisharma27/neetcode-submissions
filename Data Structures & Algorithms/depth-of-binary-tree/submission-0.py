# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ## base
        if root is None:
            return 0

        
        ## logic
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



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
#             res = max(res, depth)

#             if node:
#                 st.append([root.left, depth + 1])
#                 st.append([root.right, depth + 1])

#         return res

