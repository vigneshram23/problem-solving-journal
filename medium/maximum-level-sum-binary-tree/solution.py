from collections import deque
from typing import Optional


class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Solution to LeetCode 1161: Maximum Level Sum of a Binary Tree.
    """

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        Returns the smallest level number with the maximum sum of node values.

        Level numbering starts from 1 (root level).

        :param root: Root of the binary tree
        :return: Level number with maximum sum
        """

        # Safety check (though LeetCode guarantees at least 1 node)
        if not root:
            return 0

        queue = deque([root])
        current_level = 1

        max_sum = float("-inf")
        max_sum_level = 1

        # Breadth-First Search (Level Order Traversal)
        while queue:
            level_sum = 0
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Update only if strictly greater
            # This ensures the smallest level is returned in case of ties
            if level_sum > max_sum:
                max_sum = level_sum
                max_sum_level = current_level

            current_level += 1

        return max_sum_level
