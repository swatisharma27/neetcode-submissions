# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = float("-inf")
        self.dfs(root)
        return self.result



    def dfs(self, root):

        # base
        if root is None:
            return 0


        # logic
        leftMax = self.dfs(root.left)
        rightMax = self.dfs(root.right)
        leftMax = max(0, leftMax)
        rightMax = max(0, rightMax)

        self.result = max(self.result, root.val + leftMax + rightMax)

        return root.val + max(leftMax, rightMax)


       
