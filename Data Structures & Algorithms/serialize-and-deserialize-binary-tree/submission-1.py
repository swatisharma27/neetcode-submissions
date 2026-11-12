# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    """
    TC: O(n) - both for serialize and deserialize
    """
    
    # Encodes a tree to a single string. 
    def serialize(self, root: Optional[TreeNode]) -> str:
        ## PREORDER
        result = []

        def dfs(root):

            # base
            if root is None:
                result.append("N")
                return

            # action
            result.append(str(root.val))

            # logic
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.i = 0

        def dfs():
            # base
            if values[self.i] == "N":
                self.i += 1
                return None

            # logic
            curr = TreeNode(val = int(values[self.i]))
            self.i += 1
            curr.left = dfs()
            curr.right = dfs()

            return curr
        
        return dfs()

            









