# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []
        self.bfs(root)
        return self.result

    
    def bfs(self, root):

        # base
        if root is None:
            return 

        # logic
        q = deque()
        q.append(root)

        while q:
            size = len(q)
            new_level = []
            for _ in range(size):
                curr = q.popleft()
                new_level.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            self.result.append(new_level)

        