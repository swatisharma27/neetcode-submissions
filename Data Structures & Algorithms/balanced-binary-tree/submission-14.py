# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        return self.result
    
    def dfs(self, root):

        # base
        if not root:
            return 0

        # logic
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if abs(right - left) > 1:
            self.result = False

        output = 1 + max(left, right)
        return output



        