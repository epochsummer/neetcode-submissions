# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_minimum(self,root: Optional[TreeNode]):
        current = root
        while current.left != None:
            current = current.left
        return current

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                minimum = self.find_minimum(root.right)
                root.val = minimum.val
                root.right = self.deleteNode(root.right,minimum.val)
        return root
            
        