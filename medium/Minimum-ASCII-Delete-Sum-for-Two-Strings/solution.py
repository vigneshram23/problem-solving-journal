class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        
        dp = [0] * (n + 1)
        
        # Base case: s1 is empty
        for j in range(n - 1, -1, -1):
            dp[j] = dp[j + 1] + ord(s2[j])
        
        for i in range(m - 1, -1, -1):
            prev = dp[n]
            dp[n] += ord(s1[i])  # s2 exhausted
            
            for j in range(n - 1, -1, -1):
                temp = dp[j]
                if s1[i] == s2[j]:
                    dp[j] = prev
                else:
                    dp[j] = min(
                        ord(s1[i]) + dp[j],
                        ord(s2[j]) + dp[j + 1]
                    )
                prev = temp
        
        return dp[0]


def test():
    sol = Solution()
    
    assert sol.minimumDeleteSum("sea", "eat") == 231
    assert sol.minimumDeleteSum("delete", "leet") == 403
    assert sol.minimumDeleteSum("a", "a") == 0
    assert sol.minimumDeleteSum("a", "b") == ord('a') + ord('b')
    assert sol.minimumDeleteSum("", "abc") == ord('a') + ord('b') + ord('c')
    
    print("All tests passed!")

test()
