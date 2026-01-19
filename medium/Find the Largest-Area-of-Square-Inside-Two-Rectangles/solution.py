class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        Find the maximum area of a square that can fit inside
        the intersection of at least two rectangles.

        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        n = len(bottomLeft)
        max_area = 0

        # Check all pairs of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                # Compute intersection rectangle
                x_left = max(bottomLeft[i][0], bottomLeft[j][0])
                y_bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                x_right = min(topRight[i][0], topRight[j][0])
                y_top = min(topRight[i][1], topRight[j][1])

                width = x_right - x_left
                height = y_top - y_bottom

                # Valid intersection
                if width > 0 and height > 0:
                    side = min(width, height)
                    max_area = max(max_area, side * side)

        return max_area
