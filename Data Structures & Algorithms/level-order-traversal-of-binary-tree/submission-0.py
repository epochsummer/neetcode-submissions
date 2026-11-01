# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst = [root]
        final = []
        current = root

        while len(lst) != 0 and current is not None:
            node_number = len(lst)
            sub = []
            for i in range(node_number):
                current = lst.pop(0)
                sub.append(current.val)

                if current.left is not None:
                    lst.append(current.left)
                if current.right is not None:
                    lst.append(current.right)
            final.append(sub)
        return final
                

        