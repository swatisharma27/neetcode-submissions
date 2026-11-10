# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def __init__(self):
    #     self.result = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = self.dfs(root)
        if result != -1:
            return True
        return False
    
    def dfs(self, root):

        # base
        if not root:
            return 0

        # logic
        left = self.dfs(root.left)
        if left == -1:
            return -1
        right = self.dfs(root.right)
        if right == -1:
            return -1

        if abs(right - left) > 1:
           return -1

        output = 1 + max(left, right)
        return output



        