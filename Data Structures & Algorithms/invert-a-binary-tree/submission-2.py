# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return 

        if root.left is not None:
            root.left = self.invertTree(root.left)
        if root.right is not None:
            root.right = self.invertTree(root.right)
        
        if root.left is not None and root.right is not None:
            root.left, root.right = root.right,root.left
        elif root.left == None and root.right != None:
            root.left = root.right
            root.right = None
        elif root.right == None and root.left != None:
            root.right = root.left
            root.left = None
        return root
        
        