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

        if left >= root.val or right <= root.val:
            return False

        # logic
        left = self.dfs(left, root.left, root.val)
        right = self.dfs(root.val, root.right, right)

        return left and right
