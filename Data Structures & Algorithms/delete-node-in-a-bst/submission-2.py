# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # base
        if root is None:
            return

        # logic
        if key > root.val:
            # go right
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            # go left
            root.left = self.deleteNode(root.left, key)

        else:
            # we find the key to remove
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Find the min from the right subtree
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = self.deleteNode(root.right, root.val)

        return root


