class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n, m = len(nums1), len(nums2)
        NEG_INF = -10**18
        
        # dp[i][j] = max dot product from nums1[i:] and nums2[j:]
        dp = [[NEG_INF] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                product = nums1[i] * nums2[j]
                
                take_both = product + max(0, dp[i + 1][j + 1])
                skip_nums1 = dp[i + 1][j]
                skip_nums2 = dp[i][j + 1]
                
                dp[i][j] = max(take_both, skip_nums1, skip_nums2)
        
        return dp[0][0]
