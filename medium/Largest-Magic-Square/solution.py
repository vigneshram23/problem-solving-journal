"""
----------------------------------
Find the largest k x k magic square in a grid.
"""

class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        # Prefix sums for rows and columns
        row_prefix = [[0] * (n + 1) for _ in range(m)]
        col_prefix = [[0] * n for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j]
                col_prefix[i + 1][j] = col_prefix[i][j] + grid[i][j]

        # Try larger squares first
        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):

                    target = row_prefix[r][c + k] - row_prefix[r][c]
                    valid = True

                    # Check row sums
                    for i in range(r, r + k):
                        if row_prefix[i][c + k] - row_prefix[i][c] != target:
                            valid = False
                            break
                    if not valid:
                        continue

                    # Check column sums
                    for j in range(c, c + k):
                        if col_prefix[r + k][j] - col_prefix[r][j] != target:
                            valid = False
                            break
                    if not valid:
                        continue

                    # Check main diagonal
                    diag1 = sum(grid[r + i][c + i] for i in range(k))
                    if diag1 != target:
                        continue

                    # Check anti-diagonal
                    diag2 = sum(grid[r + i][c + k - 1 - i] for i in range(k))
                    if diag2 != target:
                        continue

                    return k

        # Every single cell is a magic square
        return 1
