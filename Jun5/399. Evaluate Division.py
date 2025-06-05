class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (a,b),val  in zip(equations,values) :
            graph[a][b] =val
            graph[b][a]=1/val

    #     graph = {
    # "a": {"b": 2.0},
    # "b": {"a": 0.5}
    # }
        
        def dfs(curr,end,visited):

            if curr not in graph or end not in graph:
                return -1

            if curr==end:
                return 1
            visited.add(curr)            

            for neighbor,val in graph[curr].items():
                if neighbor in visited:
                    continue
                result =dfs(neighbor,end,visited)
              
                if result!=-1:
                    return result *val
            return -1

        ret=[]
        for x,y in queries:
            ret.append(dfs(x,y,set()))
        return ret