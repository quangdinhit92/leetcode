class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            graph[edge[0]].append(edge[1])
            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[1]].append(edge[0])

        visited = set()

        def dfs(v, path):
            path.append(v)

            if len(path) > n:
                return False

            if v == destination:
                return True
            ret = False
            for neighbor in graph[v]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    ret |= dfs(neighbor, path)
            return ret

        visited.add(source)
        return dfs(source, [])
