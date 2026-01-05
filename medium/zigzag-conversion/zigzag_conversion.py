"""
Zigzag Conversion

Convert a string into a zigzag pattern across multiple rows and
read line by line.

Author: Vignesh R
"""

from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert a string into zigzag format.

        Args:
            s (str): Input string
            numRows (int): Number of rows for zigzag pattern

        Returns:
            str: Zigzag converted string

        Time Complexity:
            O(n)

        Space Complexity:
            O(n)
        """

        # Edge case: zigzag not possible
        if numRows == 1 or numRows >= len(s):
            return s

        rows: List[str] = [""] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char

            # Reverse direction at top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            current_row += 1 if going_down else -1

        return "".join(rows)
