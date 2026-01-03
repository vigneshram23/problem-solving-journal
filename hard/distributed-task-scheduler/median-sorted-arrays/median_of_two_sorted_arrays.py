"""
Median of Two Sorted Arrays (Hard)

This module provides an optimal solution to find the median of two
sorted arrays in O(log(min(m, n))) time complexity.

Author: Vignesh R
"""

from typing import List


class Solution:
    """
    Provides method to compute median of two sorted arrays.
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find the median of two sorted arrays.

        Args:
            nums1 (List[int]): First sorted array.
            nums2 (List[int]): Second sorted array.

        Returns:
            float: Median of the combined sorted arrays.

        Time Complexity:
            O(log(min(m, n)))

        Space Complexity:
            O(1)
        """

        # Ensure nums1 is the smaller array for optimized binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # Handle edge boundaries using +/- infinity
            max_left_1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            min_right_1 = float("inf") if partition1 == m else nums1[partition1]

            max_left_2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            min_right_2 = float("inf") if partition2 == n else nums2[partition2]

            # Check if correct partition is found
            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                # Even total length
                if (m + n) % 2 == 0:
                    return (
                        max(max_left_1, max_left_2)
                        + min(min_right_1, min_right_2)
                    ) / 2.0
                # Odd total length
                return float(max(max_left_1, max_left_2))

            # Move binary search boundaries
            elif max_left_1 > min_right_2:
                high = partition1 - 1
            else:
                low = partition1 + 1

        # Should never reach here for valid inputs
        raise ValueError("Input arrays are not sorted or invalid.")
