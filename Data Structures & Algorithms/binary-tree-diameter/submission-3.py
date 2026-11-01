# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum = 0
        def dfs(root):
            nonlocal maximum
            
            if root == None:
                return 0
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            height = max(left_height,right_height)
            diameter = left_height + right_height

            maximum = max(maximum,diameter,height)

            return height + 1
        dfs(root)
        return maximum

        