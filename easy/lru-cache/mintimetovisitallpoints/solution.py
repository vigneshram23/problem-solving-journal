class Solution:
    def minTimeToVisitAllPoints(self, points):
        """
        Calculate the minimum time required to visit all points
        in the given order on a 2D plane.

        Movement rules:
        - 1 second to move horizontally by 1 unit
        - 1 second to move vertically by 1 unit
        - 1 second to move diagonally (1 unit x + 1 unit y)

        :param points: List[List[int]] - list of [x, y] coordinates
        :return: int - minimum time in seconds
        """
        if not points or len(points) == 1:
            return 0

        total_time = 0

        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)

            # Minimum time between two points
            total_time += max(dx, dy)

        return total_time


if __name__ == "__main__":
    sol = Solution()

    assert sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]) == 7
    assert sol.minTimeToVisitAllPoints([[3,2],[-2,2]]) == 5
    assert sol.minTimeToVisitAllPoints([[0,0]]) == 0
    assert sol.minTimeToVisitAllPoints([[0,0],[1,1],[1,2]]) == 2

    print("All tests passed ✅")


