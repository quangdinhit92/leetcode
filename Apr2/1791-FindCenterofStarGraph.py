class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        firstNode = edges[0][0]
        secondNode = edges[0][1]
        secondedge = edges[1]

        if firstNode in secondedge:
            return firstNode
        return secondNode

        # nodes ={}
        # for edge in edges:
        #     fromNode=edge[0]-1
        #     toNode=edge[1]-1
        #     nodes[fromNode]= nodes.get(fromNode,0)+1
        #     nodes[toNode]= nodes.get(toNode,0)+1

        # n = len(nodes)

        # for k,v in nodes.items():
        #     if v == n-1:
        #         return k+1
        # return -1
