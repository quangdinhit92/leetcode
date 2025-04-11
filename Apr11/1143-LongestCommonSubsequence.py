class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1] * n for _ in range(m)]

        def dfs(i, j):

            if i >= m or j >= n:
                return 0

            if -1 != dp[i][j]:
                return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = 1 + dfs(i + 1, j + 1)
            else:
                dp[i][j] = max(dfs(i + 1, j), dfs(i, j + 1))
            return dp[i][j]

        return dfs(0, 0)
