"""
Longest Palindromic Substring
-----------------------------
LeetCode Problem #5 (Medium)

Given a string s, return the longest palindromic substring in s.

This implementation uses the "Expand Around Center" technique,
which is optimal for the given constraints.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        Finds the longest palindromic substring in the given string.

        :type s: str
        :rtype: str
        """

        if not s or len(s) < 2:
            return s

        start = 0
        max_length = 1
        n = len(s)

        for i in range(n):
            # Case 1: Odd-length palindrome (center at i)
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                current_length = right - left + 1
                if current_length > max_length:
                    max_length = current_length
                    start = left
                left -= 1
                right += 1

            # Case 2: Even-length palindrome (center between i and i+1)
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                current_length = right - left + 1
                if current_length > max_length:
                    max_length = current_length
                    start = left
                left -= 1
                right += 1

        return s[start:start + max_length]


if __name__ == "__main__":
    # Basic manual tests
    solution = Solution()
    print(solution.longestPalindrome("babad"))  # Expected: "bab" or "aba"
    print(solution.longestPalindrome("cbbd"))   # Expected: "bb"
    print(solution.longestPalindrome("a"))      # Expected: "a"
    print(solution.longestPalindrome("ac"))     # Expected: "a"
