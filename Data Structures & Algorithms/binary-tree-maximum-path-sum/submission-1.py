# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val
        self.dfs(root)
        return self.result


    def dfs(self, root):

        # base
        if root is None:
            return 0

        # logic
        leftMax = self.dfs(root.left)
        rightMax = self.dfs(root.right)

        # negative values won't add to maximum so make them 0
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        self.result = max(self.result, root.val + leftMax + rightMax)

        return root.val + max(leftMax, rightMax)



