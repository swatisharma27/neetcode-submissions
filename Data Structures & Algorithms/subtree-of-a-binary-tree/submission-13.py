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
        if subRoot is None:
            return True

        if root is None:
            return False

        # action
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True

        # logic
        left = self.dfs(root.left, subRoot)
        right = self.dfs(root.right, subRoot)

        return left or right


    def isSameTree(self, p, q):
        return self.dfs_same_tree(p, q)


    def dfs_same_tree(self, p, q):

        # base
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        # logic
        if p.val != q.val:
            return False

        left = self.dfs_same_tree(p.left, q.left)
        right = self.dfs_same_tree(p.right, q.right)

        return left and right