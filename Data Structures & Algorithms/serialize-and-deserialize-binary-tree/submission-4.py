# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:

    # Encodes a tree to a single string. 
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.result = []
        self.dfs_slz(root)
        return ",".join(self.result)

    def dfs_slz(self, root):

        # base
        if root is None:
           self.result.append("N")
           return self.result

        # action - processing the nodes
        self.result.append(str(root.val))

        # logic - traversal
        self.dfs_slz(root.left)
        self.dfs_slz(root.right)

       
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        self.values = data.split(",")
        self.i = 0 
        return self.dfs_deslz()       
    
    def dfs_deslz(self):

        # base
        if self.values[self.i] == "N":
            self.i += 1
            return

        # logic
        node = TreeNode(int(self.values[self.i]))
        self.i += 1

        node.left = self.dfs_deslz()
        node.right = self.dfs_deslz()

        return node



        























