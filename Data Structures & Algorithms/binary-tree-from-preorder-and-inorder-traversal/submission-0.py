# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorderIndx = 0

        inorderMap = {}
        for idx, element in enumerate(inorder):
            inorderMap[element]=idx

        return self.helper(preorder, inorder, inorderMap, 0, len(inorder)-1)


    def helper(self, preorder, inorder, inorderMap, start, end):

        # base
        if start > end:
            return None

        # logic
        root_val = preorder[self.preorderIndx]
        self.preorderIndx += 1

        root = TreeNode(root_val)
        mid = inorderMap[root_val]

        root.left = self.helper(preorder, inorder, inorderMap, start, mid-1)
        root.right = self.helper(preorder, inorder, inorderMap, mid+1, end)

        return root








        
        
