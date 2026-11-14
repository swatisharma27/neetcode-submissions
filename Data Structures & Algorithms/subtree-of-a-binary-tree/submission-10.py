# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    """
    TC: O(N * M); for each tree in the main node we will have to traverse N nodes in the subRoot tree
    SC: O(H + K); H for main tree, K for subRoot tree
    """

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)


    def isSameTree(self, p, q):

        # base
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        # action
        if p.val != q.val:
            return False

        # logic
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right
    
    def dfs(self, root, subRoot):

        # base
        if root is None and subRoot is not None:
            return False

        if subRoot is None and root is not None:
            return True

        if subRoot is None and root is None:
            return True     

        # action
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True

        left = self.dfs(root.left, subRoot)
        right = self.dfs(root.right, subRoot)

        return left or right
        
        