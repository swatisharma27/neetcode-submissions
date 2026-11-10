# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # base
        if root is None or root == p or root == q:
            return root

        # logic
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # action
        if left is None and right is None:
            return None
        elif left is not None and right is None:
            return left
        elif left is None and right is not None:
            return right
        else:
            return root


    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ## this is when the tree is BST
    #     # base
    #     if root is None:
    #         return None

    #     # logic
    #     if p.val < root.val and q.val < root.val:
    #         return self.lowestCommonAncestor(root.left, p, q)

    #     elif p.val > root.val and q.val > root.val:
    #         return self.lowestCommonAncestor(root.right, p, q)

    #     else:
    #         return root

    