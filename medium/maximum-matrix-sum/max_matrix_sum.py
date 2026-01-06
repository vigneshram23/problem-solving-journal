"""
Problem: Maximum Matrix Sum (LeetCode 1975)

You are given an n x n integer matrix.
You may repeatedly flip the signs of any two adjacent elements.
Your goal is to maximize the total sum of the matrix.

This implementation focuses on:
- Clarity
- Performance
- Production-level readability
"""

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
        Computes the maximum possible matrix sum after applying
        the allowed sign-flipping operations.

        :param matrix: n x n matrix of integers
        :return: maximum achievable sum
        """

        total_sum = 0
        negative_count = 0
        min_absolute_value = float("inf")

        for row in matrix:
            for value in row:
                absolute_value = abs(value)
                total_sum += absolute_value

                if value < 0:
                    negative_count += 1

                if absolute_value < min_absolute_value:
                    min_absolute_value = absolute_value

        # If the number of negative elements is odd,
        # one smallest absolute value must remain negative
        if negative_count % 2 != 0:
            total_sum -= 2 * min_absolute_value

        return total_sum


if __name__ == "__main__":
    # Basic sanity tests
    solution = Solution()

    assert solution.maxMatrixSum([[1, -1], [-1, 1]]) == 4
    assert solution.maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) == 16
    assert solution.maxMatrixSum([[-1, 0], [2, 3]]) == 6

    print("All test cases passed successfully.")
