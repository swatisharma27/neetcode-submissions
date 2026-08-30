# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.flag = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.helper(root)
        return self.flag

    def helper(self, node):

        # base
        if node is None:
            return 0

        # logic
        left = self.helper(node.left)
        right = self.helper(node.right)

        if left is not None and right is not None:
            if (left-right) > 1 or (right-left) > 1:
                self.flag = False

        return 1 + max(left, right)
