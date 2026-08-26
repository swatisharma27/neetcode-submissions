# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.flag = True
        self.prev = None


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.helper(root)
        return self.flag

    
    def helper(self, root):

        # base case
        if root is None or not self.flag:
            return 

        # logic
        self.helper(root.left)

        if self.prev is not None and self.prev.val >= root.val:
            self.flag = False

        self.prev = root
        self.helper(root.right)
