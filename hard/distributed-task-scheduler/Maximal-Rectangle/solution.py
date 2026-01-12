from typing import List


class Solution:
    """
    Computes the area of the largest rectangle containing only 1's
    in a binary matrix.
    """

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Given a rows x cols binary matrix filled with '0's and '1's,
        return the area of the largest rectangle containing only '1's.

        Approach:
        - Treat each row as the base of a histogram.
        - Build heights column-wise.
        - For each row, compute the largest rectangle in histogram
          using a monotonic stack.

        :param matrix: List[List[str]]
        :return: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for r in range(rows):
            # Step 1: Update histogram heights
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0

            # Step 2: Largest Rectangle in Histogram
            stack = []
            for i in range(cols + 1):
                current_height = heights[i] if i < cols else 0

                while stack and current_height < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)

                stack.append(i)

        return max_area
