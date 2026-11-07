# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        self.result = []
        self.dfs(root)
        return self.result        

    def dfs(self, root):

        """
        TC: O(n)
        SC: O(h)
        """

        # base
        if root is None:
            return


        # logic
        self.result.append(root.val)

        self.dfs(root.left)
        self.dfs(root.right)


