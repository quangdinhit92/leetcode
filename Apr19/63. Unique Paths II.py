class Solution:
    # Top down
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     m= len(obstacleGrid)
    #     n= len(obstacleGrid[0])
    #     dp =[[0]*n for _ in range(m)]
    #     dp[m-1][n-1]=1

    #     if 1== obstacleGrid[m-1][n-1]:
    #         return 0

    #     for i in range(m-1,-1,-1):
    #         for j in range(n-1,-1,-1):
                
    #             if i+1<m and obstacleGrid[i][j]!=1:
    #                 dp[i][j] +=dp[i+1][j]
    #             if j+1<n and obstacleGrid[i][j]!=1:
    #                 dp[i][j] +=dp[i][j+1]
    #     return dp[0][0]
    # bottom up
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m= len(obstacleGrid)
        n= len(obstacleGrid[0])
        dp =[[0]*n for _ in range(m)]
        
        def dfs(x,y):
            if x>=m or y>=n or obstacleGrid[x][y]==1 :
                return 0
           
            if x==m-1 and y==n-1:
                return 1
            if dp[x][y]!=0:
                return dp[x][y]
            dp[x][y]=dfs(x+1,y)+dfs(x,y+1)
            return dp[x][y]
        
        return dfs(0,0)
        