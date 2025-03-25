class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0] * (n + 1)

        # for i in range(1,n+1):
        #     #neu i la so chan thi so luong so 1 khong doi , chi them 0 vao sau
        #     #dp[4] == dp[2]
        #     #neu i la so le thi dp[i] = so truoc no +1
        #     if i%2==0:
        #         dp[i] = dp[i//2]
        #     else:
        #         dp[i] = dp[i-1]+1
        # return dp

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (1 & i)
        return dp
