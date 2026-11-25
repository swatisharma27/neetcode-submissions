# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None
        self.flag = False
        self.dfs(root, k)
        return self.result
        

    def dfs(self, root, k):

        # base
        if root is None:
            return

        # logic
        if not self.flag:
            self.dfs(root.left, k)

        self.count += 1
        if self.count == k:
            self.result = root.val
            self.flag = True

        if not self.flag:
            self.dfs(root.right, k)

