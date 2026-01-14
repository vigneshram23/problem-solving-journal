class Solution(object):
    def separateSquares(self, squares):
        """
        Find the minimum y-coordinate such that the total area of squares
        above the horizontal line equals the total area below it.

        Sweep-line approach:
        - Convert squares into vertical events.
        - Integrate area using prefix widths.
        """

        events = []
        total_area = 0.0

        # Create sweep events
        for _, y, l in squares:
            events.append((y, l))       # square starts contributing
            events.append((y + l, -l))  # square stops contributing
            total_area += l * l

        # Sort events by y-coordinate
        events.sort()

        target_area = total_area / 2.0

        curr_rate = 0.0     # total active width at current sweep height
        area_below = 0.0    # accumulated area below current y
        prev_y = events[0][0]

        # Sweep from bottom to top
        for y, delta in events:
            height = y - prev_y

            if height > 0 and curr_rate > 0:
                segment_area = curr_rate * height

                # Check if target area lies in this segment
                if area_below + segment_area >= target_area:
                    return prev_y + (target_area - area_below) / curr_rate

                area_below += segment_area

            curr_rate += delta
            prev_y = y

        return prev_y
