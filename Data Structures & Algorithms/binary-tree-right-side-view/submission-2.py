# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.bfs(root)
        return self.result


    def bfs(self, root):

        # base
        if root is None:
            return None

        # logic
        q = deque()
        q.append(root)

        while q:
            size = len(q)
            new = []

            for _ in range(size):
                curr = q.popleft()
                new.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            self.result.append(new[-1])
        
