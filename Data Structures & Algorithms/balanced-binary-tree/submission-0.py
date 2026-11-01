# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        boolean = True
        def height(root):
            nonlocal boolean
            if root == None:
                return 0
            left_level = height(root.left)
            right_level = height(root.right)

            if boolean == True:
                if abs(right_level - left_level) > 1:
                    boolean = False
            
            return max(left_level,right_level) + 1
        height(root)
        return boolean
    
        