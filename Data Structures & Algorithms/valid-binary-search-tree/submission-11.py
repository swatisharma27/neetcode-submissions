# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    TC: O(n)
    SC: O(h) ; worst case O(n) as tree can be skewed
    """

    def __init__(self):
        self.flag = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.dfs(float("-inf"), root, float("inf"))
        return self.flag


    def dfs(self, left, root, right):

        # base
        if root is None:
            return 


        # logic
        if self.flag:
            self.dfs(left, root.left, root.val)


        if left >= root.val or root.val >= right:
            self.flag = False

        if self.flag:
            self.dfs(root.val, root.right, right)

        


























    #     return self.dfs(float("-inf"), root, float("inf"))
        
    # def dfs(self, left, root, right):

    #     # base
    #     if root is None:
    #         return True

    #     if left >= root.val or right <= root.val:
    #         return False

    #     # logic
    #     left = self.dfs(left, root.left, root.val)
    #     right = self.dfs(root.val, root.right, right)

    #     return left and right
