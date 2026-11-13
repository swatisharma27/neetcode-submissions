# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        self.dfs(float("-inf"), root, float("inf"))
        return self.flag


    def dfs(self, left, root, right):

        # base
        if root is None:
            return True

        # logic
        if left >= root.val or root.val >= right:
            self.flag = False
            return
        
        if self.flag:
            self.dfs(left, root.left, root.val)
            self.dfs(root.val, root.right, right)


















