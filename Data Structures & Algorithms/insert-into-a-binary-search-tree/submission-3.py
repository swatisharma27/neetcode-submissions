# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.dfs(root, val)



    def dfs(self, root, val):

        # base
        if root is None:
            return TreeNode(val)

        # logic
        if val < root.val:
            root.left = self.dfs(root.left, val)

        elif val > root.val:
            root.right = self.dfs(root.right, val)

        return root

        
