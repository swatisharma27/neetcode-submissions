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
        left = self.dfs(root.left)
        leftMax = max(left, 0)
        right = self.dfs(root.right)
        rightMax = max(right, 0)

        output = root.val + leftMax + rightMax
        self.result = max(output, self.result)

        return root.val + max(leftMax, rightMax)




       
