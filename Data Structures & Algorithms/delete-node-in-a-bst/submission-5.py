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
            return None


        # action
        if key < root.val:
            # key to be deleted is on the left side
            root.left = self.dfs(root.left, key)
        elif key > root.val:
            # key to be deleted is on the right side
            root.right = self.dfs(root.right, key)
        else:

            # left child only
            if root.right is None:
                return root.left

            # right child only
            elif root.left is None:
                return root.right

            # both childs
            else:
                # right subtree
                curr = root.right
                while curr.left:
                    curr = curr.left

                root.val = curr.val
                root.right = self.dfs(root.right, root.val)


        return root

        