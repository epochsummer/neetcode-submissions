# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root,subroot):
            if root is None and subroot is None:
                return True
            if root is not None and subroot is not None:
                left = sameTree(root.left,subroot.left)
                right = sameTree(root.right,subroot.right)
                return (root.val == subroot.val
                and left and right)
            else:
                return False
        
        if root.val == subRoot.val:
            if sameTree(root,subRoot):
                return True
        if root.left is not None:
            if self.isSubtree(root.left,subRoot):
                return True
        if root.right is not None:
            if self.isSubtree(root.right,subRoot):
                return True
        return False
        



        