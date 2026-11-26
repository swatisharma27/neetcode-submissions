# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.dfs(root, key)

    
    def dfs(self, root, key):

        # base
        if root is None:
            return 

        # logic
        if key < root.val:
            # left subtree
            root.left = self.dfs(root.left, key)
        elif key > root.val:
            # right subtree 
            root.right = self.dfs(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left

                root.val = curr.val
                root.right = self.dfs(root.right, root.val)
        
        return root

        

       