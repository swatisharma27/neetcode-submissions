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
        self.helper(root, float("-inf"))
        return self.count
        
    def helper(self, root, maxVal):

        # base
        if root is None:
            return

        # logic
        if root.val >= maxVal:
            maxVal = root.val
            self.count += 1

        self.helper(root.left, maxVal)
        self.helper(root.right, maxVal)
