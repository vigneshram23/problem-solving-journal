class Solution(object):
    def minBitwiseArray(self, nums):
        """
        Construct the minimum bitwise array such that:
        ans[i] OR (ans[i] + 1) == nums[i]

        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for n in nums:
            # If n is even, it's impossible
            if n % 2 == 0:
                result.append(-1)
                continue

            # Count trailing 1s using bit manipulation
            xor_val = n ^ (n + 1)
            trailing_ones = xor_val.bit_length() - 1

            # Minimum valid ans[i]
            min_value = n - (1 << (trailing_ones - 1))
            result.append(min_value)

        return result
