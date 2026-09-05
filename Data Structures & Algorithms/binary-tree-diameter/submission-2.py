# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def __init__(self):
#         self.result = 0

#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         self.helper(root)
#         return self.result


#     def helper(self, root):

#         # base case
#         if root is None:
#             return 0


#         # logic
#         left = self.helper(root.left)
#         right = self.helper(root.right)

#         self.result = max(self.result, left + right)

#         return 1 + max(left, right)


class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.helper(root)
        return self.result


    def helper(self, root):

        # base
        if root is None:
            return 0

        # logic
        left = self.helper(root.left)
        right = self.helper(root.right)

        self.result = max(self.result, left+right)

        return 1 + max(left, right)






