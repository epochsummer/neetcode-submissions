class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def find(node, path_max):
            if node is None:
                return 0

            # Count the current node if it is good.
            number = 0
            if node.val >= path_max:
                number = 1

            # Include this node in the maximum for its children.
            path_max = max(path_max, node.val)

            left = find(node.left, path_max)
            right = find(node.right, path_max)

            return number + left + right

        return find(root, root.val)