# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left = float("-inf")
        right = float("inf")
        return self.dfs(left, root, right)


    def dfs(self, left, root, right):

        # base
        if root is None:
            return True

        if left >= root.val or root.val >= right:
            return False

        # logic
        l = self.dfs(left, root.left, root.val)
        r = self.dfs(root.val, root.right, right)

        return l and r