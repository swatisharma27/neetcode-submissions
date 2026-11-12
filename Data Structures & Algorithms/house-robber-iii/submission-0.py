# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        withRoot = 0
        withoutRoot = 0
        output = [withRoot, withoutRoot]
        result = self.dfs(root, output)
        return max(result)


    def dfs(self, root, output):

        # base
        if root is None:
            return [0, 0]

        # logic
        leftA, leftB = self.dfs(root.left, output)
        rightA, rightB = self.dfs(root.right, output)

        withRoot = root.val + leftB + rightB
        withoutRoot = max(leftA, leftB) + max(rightA, rightB)

        return [withRoot, withoutRoot]


        

