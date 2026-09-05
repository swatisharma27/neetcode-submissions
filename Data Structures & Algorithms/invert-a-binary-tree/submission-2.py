# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

#         ## base
#         if root is None:
#             return

#         ## logic
#         temp = root.left
#         root.left = root.right
#         root.right = temp

#         # root.left, root.right = root.right, root.left

#         self.invertTree(root.left)
#         self.invertTree(root.right)

#         return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.helper(root)
        return root

    
    def helper(self, root):
        
        ## base
        if root is None:
            return

        ## logic
        self.helper(root.left)
        self.helper(root.right)

        root.left, root.right = root.right, root.left

        