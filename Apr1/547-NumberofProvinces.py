class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        visited = set()
        count = 0

        def dfs(v):
            for i in range(n):
                if isConnected[v][i] == 1 and i not in visited:
                    visited.add(i)
                    dfs(i)

        for v in range(n):
            if v not in visited:
                count += 1
                visited.add(v)
                dfs(v)
        return count
