"""
Separate Squares II

This module provides a sweep-line based solution to find the minimum y-coordinate
of a horizontal line that splits the union area of multiple (possibly overlapping)
squares into two equal halves.

Author: VR
"""

class Solution(object):
    def separateSquares(self, squares):
        """
        Find the minimum y-coordinate such that the union area of squares
        above the line equals the union area below the line.

        :param squares: List[List[int]] where each entry is [x, y, side_length]
        :return: float (minimum y-coordinate)
        """

        # -------------------------------
        # Step 1: Build sweep-line events
        # -------------------------------
        # Each square contributes:
        #   + start event at y
        #   + end event at y + l
        events = []
        for x, y, l in squares:
            events.append((y, x, x + l, 1))       # square enters
            events.append((y + l, x, x + l, -1))  # square leaves

        events.sort()

        # ---------------------------------------
        # Helper: Compute union length of intervals
        # ---------------------------------------
        def compute_union_length(intervals):
            """
            Computes total length covered by union of x-intervals.
            Overlapping intervals are counted only once.
            """
            if not intervals:
                return 0

            intervals.sort()
            total_length = 0
            cur_start, cur_end = intervals[0]

            for start, end in intervals[1:]:
                if start > cur_end:
                    total_length += cur_end - cur_start
                    cur_start, cur_end = start, end
                else:
                    cur_end = max(cur_end, end)

            total_length += cur_end - cur_start
            return total_length

        # ---------------------------------------
        # Step 2: First sweep to compute total area
        # ---------------------------------------
        active_intervals = []
        prev_y = events[0][0]
        total_area = 0

        for y, x1, x2, event_type in events:
            height = y - prev_y
            if height > 0:
                width = compute_union_length(active_intervals)
                total_area += width * height

            if event_type == 1:
                active_intervals.append((x1, x2))
            else:
                active_intervals.remove((x1, x2))

            prev_y = y

        half_area = total_area / 2.0

        # ------------------------------------------------
        # Step 3: Second sweep to find split y-coordinate
        # ------------------------------------------------
        active_intervals = []
        prev_y = events[0][0]
        area_below = 0

        for y, x1, x2, event_type in events:
            height = y - prev_y
            if height > 0:
                width = compute_union_length(active_intervals)
                segment_area = width * height

                if area_below + segment_area >= half_area:
                    # Linear interpolation inside this segment
                    return prev_y + (half_area - area_below) / width

                area_below += segment_area

            if event_type == 1:
                active_intervals.append((x1, x2))
            else:
                active_intervals.remove((x1, x2))

            prev_y = y

        return prev_y
