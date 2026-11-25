# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(float("-inf"), root, float("inf"))
    
    
    def dfs(self, left, root, right):

        # base
        if root is None:
            return True


        # action
        if left >= root.val or root.val >= right:
            return False

        l = self.dfs(left, root.left, root.val)
        r = self.dfs(root.val, root.right, right)

        return l & r


















