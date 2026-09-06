# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:

#     def __init__(self):
#         self.flag = True
#         self.prev = None


#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         self.helper(root)
#         return self.flag

    
#     def helper(self, root):

#         # base case
#         if root is None:
#             return 

#         # logic
#         if self.flag :
#             self.helper(root.left)

#         if self.prev is not None and self.prev.val >= root.val:
#             self.flag = False

#         self.prev = root
        
#         if self.flag :
#             self.helper(root.right)


class Solution:

    def isValidBST(self, root):
        return self.helper(float("-inf"), root, float("inf"))

    def helper(self, left, node, right):

        # base case
        if node is None:
            return True

        # logic
        if not(left < node.val < right):
            return False

        return (self.helper(left, node.left, node.val) and self.helper(node.val, node.right, right))


        

