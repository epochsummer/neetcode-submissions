# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        lst = []

        while queue and root is not None:
            taken = 1
            for __ in range(len(queue)):
                current = queue.pop(0)

                if taken == 1:
                    lst.append(current.val)
                    taken -= 1

                if current.right is not None:
                    queue.append(current.right)
                if current.left is not None:
                    queue.append(current.left)
        return lst
            


        