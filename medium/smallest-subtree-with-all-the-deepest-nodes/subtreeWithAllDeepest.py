from typing import Optional, Tuple


class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val: int = 0,
                 left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Finds the smallest subtree that contains all the deepest nodes
    in a binary tree.
    """

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Returns the root of the smallest subtree containing all deepest nodes.

        :param root: Root of the binary tree
        :return: TreeNode representing the smallest subtree root
        """

        def dfs(node: Optional[TreeNode]) -> Tuple[int, Optional[TreeNode]]:
            """
            Post-order DFS traversal.

            Returns:
            - depth: Maximum depth from this node downwards
            - subtree_root: Root of subtree containing all deepest nodes
            """
            if node is None:
                return 0, None

            left_depth, left_subtree = dfs(node.left)
            right_depth, right_subtree = dfs(node.right)

            # If depths are equal, current node is the LCA of deepest nodes
            if left_depth == right_depth:
                return left_depth + 1, node

            # Otherwise propagate the deeper subtree
            if left_depth > right_depth:
                return left_depth + 1, left_subtree
            else:
                return right_depth + 1, right_subtree

        return dfs(root)[1]
