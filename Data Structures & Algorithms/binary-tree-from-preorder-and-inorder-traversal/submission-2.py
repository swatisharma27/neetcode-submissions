# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # use preorder to get the root
        self.preorderIndx = 0

        # use inorder to get the mapping - left to mid | mid to right
        self.inorderMap = {}
        for indx, element in enumerate(inorder):
            self.inorderMap[element] = indx
        
        start = 0
        end = len(inorder)-1
        return self.dfs(preorder, inorder, start, end)
    

    def dfs(self, preorder, inorder, start, end):

        # base
        if start > end:
            return None

        # logic
        rootVal = preorder[self.preorderIndx]
        self.preorderIndx += 1

        root = TreeNode(val=rootVal)
        mid = self.inorderMap[rootVal]

        root.left = self.dfs(preorder, inorder, start, mid-1)
        root.right = self.dfs(preorder, inorder, mid+1, end)

        return root
        