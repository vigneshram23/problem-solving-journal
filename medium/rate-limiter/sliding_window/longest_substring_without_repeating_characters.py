"""
Problem: Longest Substring Without Repeating Characters (LeetCode #3)
Difficulty: Medium

Description:
Given a string s, find the length of the longest substring
without repeating characters.

Approach:
Sliding Window + Hash Set

Time Complexity: O(n)
Space Complexity: O(min(n, charset))
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen_chars = set()
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            # Shrink window until duplicate is removed
            while char in seen_chars:
                seen_chars.remove(s[left])
                left += 1

            seen_chars.add(char)
            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":
    # Sample test cases
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1
    print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
