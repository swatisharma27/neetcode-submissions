# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rob(self, root):

        return max(self.dfs(root))

    def dfs(self, root):

        # base 
        if root is None:
            return [0, 0]

        # logic
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        withRoot = root.val + left[1] + right[1] 
        withoutRoot = max(left) + max(right)

        return [withRoot, withoutRoot]



    









    



     

