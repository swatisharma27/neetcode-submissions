# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        prevMax = float("-inf")
        self.dfs(root, prevMax)
        return self.count
    
    def dfs(self, root, prevMax):

        # base
        if root is None:
            return 

        # logic
        if root.val >= prevMax:
            prevMax = root.val
            self.count += 1

        self.dfs(root.left, prevMax)
        self.dfs(root.right, prevMax)


