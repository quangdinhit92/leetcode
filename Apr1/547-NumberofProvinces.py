class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        count = 0
        allPath = []

        def dfs(v, path):
            path.append(v)
            for neighbor in range(n):
                if 1 == isConnected[v][neighbor] and neighbor not in visited:
                    visited.add(neighbor)
                    path.append(neighbor)
                    dfs(neighbor, path)
                    if path not in allPath:
                        allPath.append(path)
                    path.pop()
            if path not in allPath:
                allPath.append(path)

        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i, [])
        print(allPath)
        return count
