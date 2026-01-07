from solution import Solution, TreeNode
from collections import deque


def build_tree(level_order):
    if not level_order or level_order[0] is None:
        return None

    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1

    while queue and i < len(level_order):
        node = queue.popleft()

        if i < len(level_order) and level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1

        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1

    return root


if __name__ == "__main__":
    solution = Solution()

    root1 = build_tree([1, 7, 0, 7, -8, None, None])
    assert solution.maxLevelSum(root1) == 2

    root2 = build_tree([989, None, 10250, 98693, -89388, None, None, None, -32127])
    assert solution.maxLevelSum(root2) == 2

    print("All test cases passed ✅")
