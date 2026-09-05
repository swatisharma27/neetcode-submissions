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
        if not self.flag:
            return 0
        left = self.helper(node.left)

        if not self.flag:
            return 0
        right = self.helper(node.right)

        if (left-right) > 1 or (right-left) > 1:
            self.flag = False

        return 1 + max(left, right)







class Treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isBalanced(self, root):
        self.flag = True
        self.helper(root)
        return self.flag


    def helper(self, root):

        # base
        if root is None:
            return 0


        # logic
        left = self.helper(root.left)
        right = self.helper(root.right)

        if abs(left - right) > 1:
            self.flag = False

        return 1 + max(left, right)

