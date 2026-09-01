# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        TC: O(n)
        SC: O(n)
        """

        result = []
        q = deque()

        # base
        if root is None:
            return []

        # logic
        q.append(root)
        while q:
            size = len(q) 
            level = []

            for i in range(size):
                curr = q.popleft() 
                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            result.append(level)
        
        return result

               