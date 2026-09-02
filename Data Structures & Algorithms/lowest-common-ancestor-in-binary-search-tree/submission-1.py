# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

    #     # base
    #     if root is None:
    #         return None

    #     # logic
    #     if root.val > p.val and root.val > q.val:
    #         return self.lowestCommonAncestor(root.left, p , q)
    #     elif root.val < p.val and root.val < q.val:
    #         return self.lowestCommonAncestor(root.right, p , q)
    #     else:
    #         return root


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # base
        if root is None or p == root or q == root:
            return root

        # logic
        left = self.lowestCommonAncestor(root.left, p , q)
        right = self.lowestCommonAncestor(root.right, p , q)

        if left == None and right == None:
            return None
        elif left != None and right == None:
            return left
        elif left == None and right != None:
            return right
        else:
            return root

