class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for j in range(n)] for _ in range(m)]

        def dfs(r, c):

            if r == m - 1 and c == n - 1:
                return 1
            if r >= m or c >= n:
                return 0

            if -1 != dp[r][c]:
                return dp[r][c]

            dp[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[r][c]

        dp[0][0] = dfs(0, 0)

        return dp[0][0]
