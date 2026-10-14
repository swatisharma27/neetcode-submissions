# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)
        

    def dfs(self, root, subRoot):
        # base
        if not subRoot:
            return True

        if not root:
            return False

        # logic
        if root.val == subRoot.val:
            if self.sameTree(root, subRoot):
                return True

        left = self.dfs(root.left, subRoot)
        right = self.dfs(root.right, subRoot)
    
        return left or right

    def sameTree(self, p, q):

        # base
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        # logic
        left = self.sameTree(p.left, q.left)
        right = self.sameTree(p.right, q.right)

        return left and right
