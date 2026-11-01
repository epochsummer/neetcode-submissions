# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def given_path(root,node):
            lst = []
            while root is not None:
                lst.append(root)
                if root.val > node.val:
                    root = root.left
                elif root.val < node.val:
                    root = root.right
                else:
                    return lst

        p_lst = given_path(root,p)
        q_lst = given_path(root,q)
        shorter = min(len(p_lst),len(q_lst))

        for i in range(shorter):
            if (p_lst[i]).val != (q_lst[i]).val:
                return p_lst[i - 1]
        if len(p_lst) > len(q_lst):
            return q_lst[-1]
        else:
            return p_lst[-1]
