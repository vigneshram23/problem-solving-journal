"""
LeetCode 1390 – Four Divisors

Given an integer array nums, return the sum of divisors of the integers in that
array that have exactly four divisors. If there is no such integer, return 0.

This implementation uses an O(sqrt(n)) divisor scan per number and a small
cache to avoid recomputing results for repeated values (e.g., [21, 21]).

Author: Vignesh R
"""

from typing import List, Dict


class Solution:
    """
    Provides an efficient implementation for the 'Four Divisors' problem.
    """

    def __init__(self) -> None:
        # Cache to store: number -> sum of divisors if it has exactly 4 divisors, else 0
        self._cache: Dict[int, int] = {}

    def _four_divisor_sum(self, n: int) -> int:
        """
        Compute the sum of divisors of n if it has exactly 4 divisors.
        Otherwise, return 0.

        Args:
            n (int): Input number.

        Returns:
            int: Sum of divisors if n has exactly 4 divisors, else 0.

        Time Complexity:
            O(sqrt(n)) for a single n.

        Space Complexity:
            O(1) extra (excluding cache).
        """
        # Check cache first for repeated numbers.
        if n in self._cache:
            return self._cache[n]

        count = 0
        total = 0
        d = 1

        # Enumerate divisors up to sqrt(n)
        while d * d <= n:
            if n % d == 0:
                other = n // d
                if d == other:
                    # Perfect square divisor contributes once
                    count += 1
                    total += d
                else:
                    # Pair of distinct divisors: (d, other)
                    count += 2
                    total += d + other

                # Early exit: more than 4 divisors → not valid
                if count > 4:
                    self._cache[n] = 0
                    return 0
            d += 1

        result = total if count == 4 else 0
        self._cache[n] = result
        return result

    def sumFourDivisors(self, nums: List[int]) -> int:
        """
        Sum the divisors of all numbers in nums that have exactly four divisors.

        Args:
            nums (List[int]): List of integers.

        Returns:
            int: Sum of divisors over all qualifying integers.
        """
        total_sum = 0
        for num in nums:
            total_sum += self._four_divisor_sum(num)
        return total_sum
