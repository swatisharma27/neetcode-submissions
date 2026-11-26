# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preIndex = 0

        self.inorderMap = {}
        for index, value in enumerate(inorder):
            self.inorderMap[value] = index

        N = len(inorder)
        return self.dfs(preorder, inorder, 0, N-1)

    def dfs(self, preorder, inorder, start, end):

        # base
        if start > end:
            return 

        # logic
        value = preorder[self.preIndex]
        root = TreeNode(val=value)
        self.preIndex += 1
        
        mid = self.inorderMap[value]

        root.left = self.dfs(preorder, inorder, start, mid-1)
        root.right = self.dfs(preorder, inorder, mid+1, end)

        return root


