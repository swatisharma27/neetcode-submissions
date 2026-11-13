# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # root, left, right
        self.result = []
        self.dfs(root)
        return self.result


    def dfs(self, root):

        # base
        if root is None:
            return 

        # action
        self.result.append(root.val)

        # logic
        self.dfs(root.left)
        self.dfs(root.right)