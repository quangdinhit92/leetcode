# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # direction left =0, right =1
        self.l=0
        self.r=1
        self.max_len=0
        def dfs(node,direction,length):
            if None ==node :
                return
            self.max_len=max(self.max_len,length)
            if 0 == direction :
                dfs(node.right,1,length+1)
                dfs(node.left,0,1)
            elif 1 == direction:
                dfs(node.left,0,length+1)
                dfs(node.right,1,1)
        dfs(root,self.l,0)
        dfs(root,self.r,0)
        return self.max_len
