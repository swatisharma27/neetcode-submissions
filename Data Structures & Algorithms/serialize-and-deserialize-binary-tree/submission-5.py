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
        self.dfs_1(root)
        return ",".join(self.result)


    def dfs_1(self, root):

        # base
        if root is None:
            self.result.append("N")
            return

        # logic
        self.result.append(str(root.val))

        self.dfs_1(root.left)
        self.dfs_1(root.right)

       
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.values = data.split(",")
        self.i = 0
        return self.dfs_2()


    def dfs_2(self):

        # base
        if self.values[self.i] == "N":
            self.i += 1
            return 

        # logic
        root = TreeNode(self.values[self.i])
        self.i += 1

        root.left = self.dfs_2()
        root.right = self.dfs_2()

        return root









     
    
    