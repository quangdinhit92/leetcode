class Solution:
    def tribonacci(self, n: int) -> int:
        if 0 == n:
            return 0
        if 2 == n or 1 == n:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]
