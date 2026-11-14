# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    TC: O(n)
    SC: O(h)
    
    """
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))

    def dfs(self, root):

        # base
        if root is None:
            return [0, 0]

        # logic
        leftA, leftB = self.dfs(root.left)
        rightA, rightB = self.dfs(root.right)

        withRoot = root.val + leftB + rightB
        withoutRoot = max(leftA, leftB) + max(rightA, rightB)

        return withRoot, withoutRoot










    



     

