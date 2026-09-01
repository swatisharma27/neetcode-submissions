# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.helper(root, subRoot)


    def sameTree(self, p, q):

        # base
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False
        
        # logic
        if p.val != q.val:
            return False

        left = self.sameTree(p.left, q.left)
        right = self.sameTree(p.right, q.right)

        return left and right


    def helper(self, root, subRoot):

        # base
        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False


        # logic
        if root.val == subRoot.val:
            if self.sameTree(root, subRoot):
                return True

        l_outside = self.helper(root.left, subRoot)
        r_outside = self.helper(root.right, subRoot)

        return l_outside or r_outside


