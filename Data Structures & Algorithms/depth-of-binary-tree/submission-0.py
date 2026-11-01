# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            level = 0
            return level

        level_left = self.maxDepth(root.left)
        level_right = self.maxDepth(root.right)
        maximum = max(level_left,level_right)
        return maximum + 1