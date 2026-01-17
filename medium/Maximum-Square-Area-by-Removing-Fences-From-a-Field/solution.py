class Solution(object):
    """
    Solution to LeetCode 2975: Maximum Square Area by Removing Fences From a Field
    """

    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        Compute the maximum square area that can be formed by removing fences.

        :param m: int - vertical size of the field
        :param n: int - horizontal size of the field
        :param hFences: List[int] - removable horizontal fences
        :param vFences: List[int] - removable vertical fences
        :return: int - maximum square area modulo 1e9+7, or -1 if impossible
        """
        MOD = 10**9 + 7

        # Add boundary fences (cannot be removed)
        horizontal = sorted(hFences + [1, m])
        vertical = sorted(vFences + [1, n])

        # Collect all possible horizontal distances
        horizontal_distances = set()
        for i in range(len(horizontal)):
            for j in range(i + 1, len(horizontal)):
                horizontal_distances.add(horizontal[j] - horizontal[i])

        # Find the maximum distance that exists in both directions
        max_side = 0
        for i in range(len(vertical)):
            for j in range(i + 1, len(vertical)):
                side = vertical[j] - vertical[i]
                if side in horizontal_distances:
                    max_side = max(max_side, side)

        if max_side == 0:
            return -1

        return (max_side * max_side) % MOD
