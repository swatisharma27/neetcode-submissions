# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode): 
        return self.dfs(root, p, q)



    def dfs(self, root, p, q):

        # base
        if root is None or p == root or q == root:
            return root


        # logic
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)

        if left is None and right is None:
            return None

        elif left is not None and right is None:
            return left

        elif left is None and right is not None:
            return right

        else:
            return root






    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    #     return self.dfs(root, p, q)


    # def dfs(self, root, p, q):

    #     # base 
    #     if root is None:
    #         return 

    #     # logic
    #     if p.val < root.val and q.val < root.val:
    #         return self.dfs(root.left, p, q)

    #     elif p.val > root.val and q.val > root.val:
    #         return self.dfs(root.right, p, q)

    #     else:
    #         return root



   