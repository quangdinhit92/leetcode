class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for a,b in connections:
            graph[a].append((b,1))
            graph[b].append((a,0))
        
       
        def dfs(node,parent):
            change =0
            for neighbor, need_change in graph[node]  :
                if neighbor != parent:
                    change+=need_change
                    change+=dfs(neighbor,node)
            return change
        return dfs(0,-1)