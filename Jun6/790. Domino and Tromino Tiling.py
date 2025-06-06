class Solution:
    def numTilings(self, n: int) -> int:
        dp=[0]*(n+1)

        if 0==n:
            return 1
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 5
        dp[0]=1
        dp[1]=1
        dp[2] =2
        
        for i in range(3,n+1):
            dp[i] =(2*dp[i-1]+dp[i-3])%(10**9+7)
        return dp[n]