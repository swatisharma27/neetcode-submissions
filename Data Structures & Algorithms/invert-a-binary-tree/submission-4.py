# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)   


    
    def dfs(self, root):

        # base
        if root is None:
            return 

        # action
        root.left, root.right = root.right, root.left

        # logic
        self.dfs(root.left)
        self.dfs(root.right)

        return root
