# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    """
    LeetCode 1339: Maximum Product of Splitted Binary Tree

    Production notes:
    - Uses iterative traversals to avoid recursion depth issues (N up to 50k).
    - Computes total sum, then all subtree sums via postorder.
    - Maximizes product BEFORE modulo, per problem statement.
    """

    MOD = 10**9 + 7

    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        total = self._compute_total_sum(root)
        max_product = self._compute_max_split_product(root, total)
        return max_product % self.MOD

    def _compute_total_sum(self, root):
        """Iterative DFS to compute total sum of all nodes."""
        total = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            total += node.val
            # Push children
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return total

    def _compute_max_split_product(self, root, total):
        """
        Iterative postorder to compute subtree sums and track maximum split product.

        For each node's subtree sum = s, splitting above it yields product: s * (total - s).
        """
        # Postorder traversal using (node, visited) pattern.
        stack = [(root, False)]
        subtree_sum = {}  # node -> sum of subtree rooted at node
        max_product = 0

        while stack:
            node, visited = stack.pop()
            if node is None:
                continue

            if not visited:
                # Postorder: left, right, node
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
            else:
                left_sum = subtree_sum.get(node.left, 0)
                right_sum = subtree_sum.get(node.right, 0)
                s = node.val + left_sum + right_sum
                subtree_sum[node] = s

                # Consider cutting the edge connecting this subtree to its parent
                product = s * (total - s)
                if product > max_product:
                    max_product = product

        return max_product
