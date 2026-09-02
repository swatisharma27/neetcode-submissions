# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        # base
        if root is None:
            return result

        q = deque()
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

            if level:
                result.append(level[-1])
        
        return result
