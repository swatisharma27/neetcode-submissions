# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.preorderIndx = 0

        self.inorderMap = {}
        for index, val in enumerate(inorder):
           self.inorderMap[val] = index

        return self.dfs(preorder, inorder, 0, len(inorder)-1)
     

    def dfs(self, preorder, inorder, start, end):

        # base
        if start > end:
            return


        # logic
        rootval = preorder[self.preorderIndx]
        self.preorderIndx += 1

        root = TreeNode(rootval)
        mid = self.inorderMap[rootval]

        root.left = self.dfs(preorder, inorder, start, mid - 1)
        root.right = self.dfs(preorder, inorder, mid+1, end)

        return root

    
        


        