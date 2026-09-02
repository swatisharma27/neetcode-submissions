# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         self.result = []
#         self.output = 0
#         self.flag = True
#         self.helper(root, k)
#         return self.output

#     def helper(self, root, k):

#         # base
#         if root is None:
#             return 0
        
#         # logic
#         if self.flag:
#             self.helper(root.left, k)

#         ### inorder
#         self.result.append(root)
#         if k == len(self.result):
#             self.output = root.val
#             self.flag = False

#         if self.flag:
#             self.helper(root.right, k)


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.output = 0
        self.flag = True
        self.helper(root, k)
        return self.output

    def helper(self, root, k):

        # base
        if root is None:
            return 0
        
        # logic
        if self.flag:
            self.helper(root.left, k)

        self.count += 1
        if self.count == k:
            self.output = root.val 
            self.flag = False

        if self.flag:
            self.helper(root.right, k)

