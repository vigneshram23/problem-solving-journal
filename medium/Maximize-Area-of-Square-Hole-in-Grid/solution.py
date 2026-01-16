class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        Find the maximum area of a square-shaped hole in the grid.

        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """

        def max_consecutive_removed_cells(bars):
            """
            Given removable bar indices, return the maximum number of
            contiguous cells formed after removing consecutive bars.
            """
            if not bars:
                return 1

            bars.sort()
            longest_streak = 1
            current_streak = 1

            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    current_streak += 1
                    longest_streak = max(longest_streak, current_streak)
                else:
                    current_streak = 1

            # Removing k consecutive bars merges (k + 1) cells
            return longest_streak + 1

        max_height = max_consecutive_removed_cells(hBars)
        max_width = max_consecutive_removed_cells(vBars)

        side_length = min(max_height, max_width)
        return side_length * side_length
