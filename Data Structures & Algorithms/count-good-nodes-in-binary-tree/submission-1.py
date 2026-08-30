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
        
    def helper(self, root, curr):

        # base
        if root is None:
            return

        # logic
        if root.val >= curr:
            curr = root.val
            self.count += 1

        self.helper(root.left, curr)
        self.helper(root.right, curr)
