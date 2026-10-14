# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0

    def goodNodes(self, root: TreeNode) -> int:
        maxVal = float("-inf")
        self.dfs(root, maxVal)
        return self.count

    def dfs(self, root, maxVal):

        # base
        if root is None:
            return 

        if root.val >= maxVal:
            self.count += 1
            maxVal = root.val

        # logic
        self.dfs(root.left, maxVal)
        self.dfs(root.right, maxVal)


        