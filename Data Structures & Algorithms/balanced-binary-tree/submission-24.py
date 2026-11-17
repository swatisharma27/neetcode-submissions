# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        out = self.dfs(root)
        if out == -1:
            return False
        else:
            return True
       

    def dfs(self, root):

        # base
        if root is None:
            return 0

        # logic
        left = self.dfs(root.left)
        if left == -1:
            return -1
        right = self.dfs(root.right)
        if right == -1:
            return -1

        if abs(left-right) > 1:
            return -1

        return 1 + max(left, right)

















