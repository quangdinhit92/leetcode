class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # dp luu cost
        n = len(cost)
        if n < 3:
            return min(cost)
        dp = []
        dp.append(0)
        dp.append(0)
        # step i duoc buoc tu step i-1 hoac i-2
        # dp[i] luu lai cost tu dau toi step i
        for i in range(2, n + 1):
            # from step i-1
            # from step i-2
            dp.append(min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]))
        return dp[n]
