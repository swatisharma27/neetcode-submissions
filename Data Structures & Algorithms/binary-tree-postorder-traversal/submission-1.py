# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # left, right, root

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.dfs(root)
        return self.result


    def dfs(self, root):
        # base
        if root is None:
            return 

        # logic
        self.dfs(root.left)
        self.dfs(root.right)

        # action
        self.result.append(root.val)
